import 'package:flutter/material.dart';
import 'package:messaging_supabase/HomeScreen.dart';
import 'package:provider/provider.dart';
import 'package:flutter/material.dart';
import 'package:supabase/supabase.dart' hide Provider;

import 'package:provider/provider.dart';
import 'AuthService.dart';
import 'AuthenticationWrapper.dart';
class ProfileSettings extends StatelessWidget {
  final TextEditingController? nameController = TextEditingController();
  final TextEditingController? bioController = TextEditingController();
  final TextEditingController? ageController = TextEditingController();
  final TextEditingController? profilepicurlController = TextEditingController();

  @override
  Widget build(BuildContext context) {


    return Scaffold(
      appBar: AppBar(
        title: Text('Profile Settings'),
      ),
      body: FutureBuilder(
        future: AuthService().fetchUserSettings(),
        builder: (context, AsyncSnapshot<Map<String, dynamic>> snapshot) {
          if (snapshot.connectionState == ConnectionState.done) {
            if (snapshot.hasError) {
              return Text("Error: ${snapshot.error}");
            }

            if (snapshot.hasData) {
              Map<String, dynamic>? data = snapshot.data;

              nameController?.text = data?['name'] ?? '';
              bioController?.text = data?['bio'] ?? '';
              ageController?.text = data?['age']?.toString() ?? '';
              profilepicurlController?.text = data?['profilepicurl'] ?? '';

              return Column(
                children: [
                  TextFormField(
                    controller: nameController,
                    decoration: InputDecoration(labelText: 'Name'),
                  ),
                  TextFormField(
                    controller: bioController,
                    decoration: InputDecoration(labelText: 'Bio'),
                  ),
                  TextFormField(
                    controller: ageController,
                    decoration: InputDecoration(labelText: 'Age'),
                  ),
                  TextFormField(
                    controller: profilepicurlController,
                    decoration: InputDecoration(labelText: 'Profile Picture URL'),
                  ),
                  ElevatedButton(
                    onPressed: () async {
                      if (nameController!.text.isNotEmpty && bioController!.text.isNotEmpty && ageController!.text.isNotEmpty) {
                      await AuthService().updateUserSettings(

                          nameController?.text ?? '',
                          bioController?.text ?? '',
                          int.parse(ageController?.text ?? '0'),
                          profilepicurlController?.text ?? '',
                        true
                      );

                      }else {
                        ScaffoldMessenger.of(context).showSnackBar(
                            SnackBar(content: Text('Please fill out all fields before saving.'))
                        );
                      }
                      Provider.of<AppState>(context, listen: false).setCurrentScreen(AppScreen.Home);
                    },
                    child: Text('Update Profile'),
                  ),
                ],
              );
            }
          }
          return CircularProgressIndicator();
        },
      ),
    );
  }




}
