import 'package:flutter/material.dart';

import 'package:provider/provider.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:supabase_flutter/supabase_flutter.dart' hide User, Provider;
import 'AuthenticationWrapper.dart';
import 'AuthService.dart';
import 'ChatModels.dart';
import 'ChatService.dart';
import 'ChatStateProvider.dart';
import 'SwipeService.dart';
import 'UserService.dart';


void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp();
  await Supabase.initialize(
    url: 'https://epxtkpaxdrjxeoaexwqj.supabase.co',
    anonKey: 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImVweHRrcGF4ZHJqeGVvYWV4d3FqIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTE4NzQ1OTIsImV4cCI6MjAwNzQ1MDU5Mn0.wxIoWC7S_OPcidAV3R9hrEPd6odWwXmnW77Wj85QSqk',
  );
  runApp(MyApp());
}


class MyApp extends StatelessWidget {
  final AuthService _authService = AuthService();
  final UserService userService = UserService();

  Future<AppScreen> fetchInitialScreen(User? user) async {
    if (user == null) {
      return AppScreen.SignIn; // Or any default screen for not signed-in users
    }
    // Fetch the 'profileSettingsCompleted' value from your database
    // Replace the line below with actual database fetching logic
    var UserSettings = await AuthService().fetchUserSettings();
    bool profileSettingsCompleted =UserSettings["profilecompleted"];
    AuthService().updatelastonlineTime();
    if (profileSettingsCompleted) {
      return AppScreen.Conversations; //first screen
    } else {
      return AppScreen.Profile;
    }
  }

  @override
  Widget build(BuildContext context) {
    return MultiProvider(
      providers: [
        Provider<AuthService>.value(
          value: _authService,
        ),
        StreamProvider<User?>.value(value: FirebaseAuth.instance.authStateChanges(),
          initialData: null,
        ),
        Provider<UserService>.value(value: UserService()),
        Provider<SwipeService>.value(value: SwipeService()),
    ChangeNotifierProvider(create: (context) => ChatStateProvider()),  // Add this line,
      ],
      child: MaterialApp(
        title: 'Flutter Auth',
        theme: ThemeData(
          primarySwatch: Colors.blue,
          visualDensity: VisualDensity.adaptivePlatformDensity,
        ),
        home: Scaffold(
          body: StreamBuilder<User?>(
            stream: FirebaseAuth.instance.authStateChanges(),
            builder: (context, snapshot) {
              if (snapshot.connectionState == ConnectionState.active) {
                User? user = snapshot.data;

                return FutureBuilder<AppScreen>(
                  future: fetchInitialScreen(user),
                  builder: (context, snapshot) {
                    if (snapshot.connectionState == ConnectionState.waiting) {
                      return CircularProgressIndicator();
                    } else if (snapshot.hasError) {
                      return Text('Error: ${snapshot.error}');
                    } else {
                      return ChangeNotifierProvider(
                        create: (context) => AppState(currentScreen: snapshot.data!),
                        child: AuthenticationWrapper(),
                      );
                    }
                  },
                );
              } else {
                return CircularProgressIndicator();
              }
            },
          ),
        ),
      ),
    );
  }
}






//var UserSettings = await AuthService().fetchUserSettings();
//     bool profileSettingsCompleted =UserSettings["profilecompleted"];

