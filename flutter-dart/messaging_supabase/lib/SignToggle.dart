import 'package:flutter/material.dart';

import 'RegistrationScreen.dart';
import 'SignInScreen.dart';
class SignToggle extends StatefulWidget {
  @override
  _SignToggleState createState() => _SignToggleState();
}

class _SignToggleState extends State<SignToggle> {

  bool showSignIn = true;
  void toggleView(){
    //print(showSignIn.toString());
    setState(() => showSignIn = !showSignIn);
  }

  @override
  Widget build(BuildContext context) {
    if (showSignIn) {
      return SignInScreen(toggleView:  toggleView);
    } else {
      return RegistrationScreen(toggleView:  toggleView);
    }
  }
}