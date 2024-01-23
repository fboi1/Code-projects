import 'dart:async';

import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:messaging_supabase/RegistrationScreen.dart';
import 'package:messaging_supabase/SignInScreen.dart';
import 'package:provider/provider.dart';

import 'AuthService.dart';


import 'package:supabase/supabase.dart' hide Provider;

import 'LocalStorage.dart';
import 'ProfileCard.dart';
import 'SwipeService.dart';
import 'UserModel.dart';
import 'UserService.dart';

class HomeScreen extends StatefulWidget {
  @override
  _HomeScreenState createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  List<UserModel> _profiles = [];
  String? _lastId;

  @override
  void initState() {
    super.initState();
    _loadFromCacheOrFetch();
  }
  void _loadFromCacheOrFetch() async {
    List<UserModel> cachedProfiles = await LocalStorage.loadProfiles();
    if (cachedProfiles.isNotEmpty) {
      setState(() {
        _profiles = cachedProfiles;
      });
    } else {
      fetchNextBatch();
    }
  }
  void fetchNextBatch() {
    final authService = Provider.of<AuthService>(context, listen: false);
    final userService = Provider.of<UserService>(context, listen: false);

    authService.fetchUserSettings().then((settings) async {
      int userAge = settings['age'];
      final profilesBatch = await userService.getUserProfiles(userAge, _lastId);

      if (profilesBatch.isNotEmpty) {
        setState(() {
          _profiles.addAll(profilesBatch);
          _lastId = profilesBatch.last.id;
        });
      }
      await LocalStorage.saveProfiles(_profiles);
    });
  }

  @override
  Widget build(BuildContext context) {
    final swipeService = Provider.of<SwipeService>(context);
    final authService = Provider.of<AuthService>(context);
    return  Scaffold(
      body: _profiles.isEmpty // Check if the list is empty
          ? Center( // If yes, return a Center widget with a text message
        child: Text('No more profiles to load'),
      )
          :Stack(
        children: _profiles.map((profile) => GestureDetector(
          onHorizontalDragEnd: (details) async {
            if (details.primaryVelocity! > 0) {
              await Future.wait([
                swipeService.createSwipe(authService.currentUser!.uid, profile.id, true),
                swipeService.incrementswipescount(authService.currentUser!.uid)
              ]);

            } else {
              //await swipeService.createSwipe(authService.currentUser!.uid, profile.id, false);
              await swipeService.incrementswipescount(authService.currentUser!.uid);
            }

            // Remove the swiped profile from the list
            setState(() {
              _profiles.remove(profile);
            });
            await LocalStorage.clearProfiles();

            // If we have fewer than 3 profiles left, fetch the next batch
            if (_profiles.length < 3) {
              fetchNextBatch();
            }
          },

          child: ProfileCard(user: profile),
        )).toList().reversed.toList(),  // Reversed so that the top-most card is the first in the list
      ),

    );

  }
}

