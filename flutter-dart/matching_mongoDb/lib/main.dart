import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import 'package:realm/realm.dart';
import 'AppServices.dart';
import 'AuthWrapper.dart';
import 'SignInScreen.dart';
import 'usersn.dart';
import 'cars.dart';
import 'UserProfiles.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  runApp(
    ChangeNotifierProvider<AppServices>(
      create: (_) => AppServices(),
      child: MyApp(),
    ),
  );
}
class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Realm Flutter Todo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: AuthWrapper(),
      routes: {
        '/login': (context) => SignInScreen(),
        //'/home': (context) => HomeScreen(),
      },
    );
  }
}

