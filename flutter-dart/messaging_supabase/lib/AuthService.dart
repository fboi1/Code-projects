import 'dart:ffi';

import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:supabase_flutter/supabase_flutter.dart' hide User, Provider;
class AuthService {
  static final FirebaseAuth _firebaseAuth = FirebaseAuth.instance;
  final supabase = Supabase.instance.client;
  static Stream<User?> get authStateChanges => _firebaseAuth.authStateChanges();
  User? get currentUser => _firebaseAuth.currentUser;
  Future<User?> signIn({required String email, required String password}) async {
    try {
      UserCredential userCredential = await _firebaseAuth.signInWithEmailAndPassword(email: email, password: password);


      return userCredential.user;
    } catch (e) {
      print("Error in SignIn: $e");
      return null;
    }
  }

  Future<User?> signUp({required String email, required String password}) async {
    try {
      UserCredential userCredential = await FirebaseAuth.instance.createUserWithEmailAndPassword(email: email, password: password);

      await supabase
          .from('profiles')
          .insert({'userid': userCredential.user!.uid, 'email': email});

      return userCredential.user;
    } on FirebaseAuthException catch (e) {
      return null;
    }
  }


  Future<void> signOut() async {
    await _firebaseAuth.signOut();
  }

  Future<Map<String, dynamic>> fetchUserSettings() async {
    print(currentUser!.uid);
    try {
      final response = await supabase
          .from('profiles')
          .select()
          .eq('userid', currentUser!.uid)
          .single();

      return response as Map<String, dynamic>;
    } catch (error) {
      throw error;
    }

  }
  Future<void> updateUserSettings(

      String name,
      String bio,
      int age,
      String profilepicurl,
      bool profilecompleted
      ) async {
    await supabase
        .from('profiles')
        .upsert({
      'userid': currentUser!.uid,
      'name': name,
      'bio': bio,
      'age': age,
      'profilepicurl': profilepicurl,
      'profilecompleted': profilecompleted,
    });
  }


  Future<void> updatelastonlineTime() async {
    await supabase
        .from('profiles')
        .upsert({
      'userid': currentUser!.uid,
      'lastonline': DateTime.now().toIso8601String(),
    });
  }

  Future<Map<String, dynamic>> fetchOtherUserSettings({required String userid}) async {
    print('currentUser!.uid');
    try {
      final response = await supabase
          .from('profiles')
          .select()
          .eq('userid', userid)
          .single();

      return response as Map<String, dynamic>;
    } catch (error) {
      throw error;
    }

  }

}
