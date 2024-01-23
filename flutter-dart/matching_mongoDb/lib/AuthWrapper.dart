import 'package:flutter/material.dart';
import 'package:matching2/RegistrationScreen.dart';
import 'package:provider/provider.dart';
import 'AppServices.dart';
class AuthWrapper extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    final authService = Provider.of<AppServices>(context);

    // Return home or authenticate widget
    if (authService.currentUser != null) {
      return RegistrationScreen(); //HomeScreen
    } else {
      return RegistrationScreen(); //
    }
  }
}
