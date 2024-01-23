import 'package:flutter/material.dart';
import 'package:messaging_supabase/RegistrationScreen.dart';
import 'package:provider/provider.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'AuthService.dart';
import 'HomeScreen.dart';

class SignInScreen extends StatelessWidget {
  final TextEditingController emailController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();
  final VoidCallback toggleView;

  SignInScreen({required this.toggleView});

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
              onPressed: () async {
                final user = await context.read<AuthService>().signIn(
                  email: emailController.text.trim(),
                  password: passwordController.text.trim(),
                );

                if (user == null) {
                  print("error couldn't sign in");
                  // The user is signed in
                  // Depending on your app logic, you could navigate to a new screen here
                }
              },
              child: Text("Sign in"),
            ),
            TextButton(
              onPressed: toggleView,
              child: Text("Don't have an account? Register"),
            ),
            TextButton(
              onPressed: () {
                //context.read<AuthService>().sendPasswordResetEmail(emailController.text.trim());
              },
              child: Text("Forgot password?"),
            ),
            ElevatedButton(
              onPressed: () {
                context.read<AuthService>().signOut(); // Sign out the current user
              },
              child: Text("Sign out"),
            ),

          ],
        ),
      ),
    );
  }
}

