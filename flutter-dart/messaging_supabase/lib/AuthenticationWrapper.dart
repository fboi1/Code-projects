import 'dart:async';

import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:messaging_supabase/ConversationsScreen.dart';
import 'package:messaging_supabase/HomeScreen.dart';
import 'package:messaging_supabase/ProfileSettings.dart';
import 'package:messaging_supabase/SignInScreen.dart';
import 'package:provider/provider.dart';


import 'AuthService.dart';
import 'ChatScreen.dart';
import 'SignToggle.dart';

//========

enum AppScreen { Home, Profile,SignIn, Conversations,OtherScreen,Chat /* add more screens here */ }

class AppState extends ChangeNotifier {
  AppScreen currentScreen;
  Map<String, dynamic> screenParameters = {}; // Map to store parameters for screens

  AppState({required this.currentScreen});

  void setCurrentScreen(AppScreen screen, [Map<String, dynamic>? parameters]) {
    currentScreen = screen;

    if (parameters != null) {
      screenParameters = parameters;
    } else {
      screenParameters.clear();
    }
    notifyListeners();
  }
}

class AuthenticationWrapper extends StatefulWidget {
  @override
  _AuthenticationWrapperState createState() => _AuthenticationWrapperState();
}

class _AuthenticationWrapperState extends State<AuthenticationWrapper> {
  late PageController _pageController;
  int currentIndex = 0; // Initial screen index

  @override
  void initState() {
    super.initState();
    _pageController = PageController(initialPage: currentIndex);
  }

  @override
  Widget build(BuildContext context) {
    final user = Provider.of<User?>(context);
    final appState = Provider.of<AppState>(context);

    if (user == null) {
      return SignToggle();
    }

    if (appState.currentScreen == AppScreen.Conversations || appState.currentScreen == AppScreen.Home) {
      return PageView(
        controller: _pageController,
        onPageChanged: (index) {
          setState(() {
            currentIndex = index;
          });
          if (index == 0) {
            appState.setCurrentScreen(AppScreen.Conversations);
          } else if (index == 1) {
            appState.setCurrentScreen(AppScreen.Home);
          }
        },
        children: [
          ConversationsScreen(),
          HomeScreen(),
        ],
      );
    } else {
      return buildScreen(appState.currentScreen, appState.screenParameters);
    }
  }

  @override
  void dispose() {
    _pageController.dispose();
    super.dispose();
  }

  Widget buildScreen(AppScreen screen, Map<String, dynamic> parameters) {
    switch (screen) {
      case AppScreen.Chat:
        return ChatScreen(
          conversationId: parameters['conversationId'],
          userId: parameters['userId'],
        );
    // ... other cases ...
      default:
        return ProfileSettings();
    }
  }
}




//ElevatedButton(
//         onPressed: () async {
//           await authService.signOut();
//         },
//         child: Text("Sign Out"),
//       );
