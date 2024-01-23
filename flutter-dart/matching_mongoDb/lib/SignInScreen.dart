import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:flutter/material.dart';
import 'AppServices.dart';


class SignInScreen extends StatelessWidget {
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
              onPressed: () async {
                final user = await context.read<AppServices>().logInUserEmailPassword(
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
              onPressed: () => Navigator.of(context).pushReplacementNamed('/register'),
              child: Text("Don't have an account? Register"),
            ),
            TextButton(
              onPressed: () {
                //context.read<AppServices>().sendPasswordResetEmail(emailController.text.trim());//Password reset
              },
              child: Text("Forgot password?"),
            ),
            ElevatedButton(
              onPressed: () {
                context.read<AppServices>().logOut(); // Sign out the current user
              },
              child: Text("Sign out"),
            ),

          ],
        ),
      ),
    );
  }
}
