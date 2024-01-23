import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:realm/realm.dart';

import 'AppServices.dart';

import 'package:flutter/material.dart';
import 'package:provider/provider.dart';


class RegistrationScreen extends StatelessWidget {
  final TextEditingController emailController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: EdgeInsets.all(16),
        child: Column(
          children: [
            TextField(
              controller: emailController,
              decoration: InputDecoration(
                labelText: "Email",
              ),
            ),
            TextField(
              controller: passwordController,
              decoration: InputDecoration(
                labelText: "Password",
              ),
              obscureText: true,
            ),
            ElevatedButton(
              onPressed: () {
                context.read<AppServices>().registerUserEmailPassword(
                  email: emailController.text.trim(),
                  password: passwordController.text.trim(),
                );
              },
              child: Text("Register"),
            ),
            TextButton(
              onPressed: () => Navigator.of(context).pushReplacementNamed('/login'),
              child: Text("Already have an account? Sign in"),
            ),
          ],
        ),
      ),
    );
  }
}

