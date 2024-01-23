import 'package:flutter/material.dart';
import 'package:messaging_supabase/SignInScreen.dart';
import 'package:provider/provider.dart';

import 'AuthService.dart';

import 'package:flutter/material.dart';
import 'package:provider/provider.dart';


class RegistrationScreen extends StatelessWidget {
  final TextEditingController emailController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();
  final VoidCallback toggleView;

  RegistrationScreen({required this.toggleView});
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
              onPressed: () async{
                final user = await context.read<AuthService>().signUp(
                  email: emailController.text.trim(),
                  password: passwordController.text.trim(),
                );

              },
              child: Text("Register"),
            ),
            TextButton(
              onPressed: toggleView,
              child: Text("Already have an account? Sign in"),
            ),
          ],
        ),
      ),
    );
  }
}

