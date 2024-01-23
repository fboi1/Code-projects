import 'package:flutter/material.dart';
import 'UserModel.dart';

class ProfileCard extends StatelessWidget {
  final UserModel user;

  const ProfileCard({Key? key, required this.user}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Column(
        children: [
          if (user.profilepicurl != null)
            Image.network(user.profilepicurl!)
          else
            Icon(Icons.account_circle, size: 100),
          Text(user.name),
          Text(user.age.toString()),
          Text(user.bio),
        ],
      ),
    );
  }
}