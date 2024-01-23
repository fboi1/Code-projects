import 'package:flutter/material.dart';
import 'package:messaging_supabase/AuthService.dart';
import 'package:supabase/supabase.dart' hide Provider;
import 'package:provider/provider.dart';
import 'package:messaging_supabase/ChatScreen.dart';
import 'AuthenticationWrapper.dart';
import 'ChatScreen.dart';
import 'ChatStateProvider.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:messaging_supabase/ChatModels.dart';


class ConversationsScreen extends StatelessWidget {
  // Assuming you pass the userId when navigating to this screen
  final String userId = AuthService().currentUser!.uid;
  ConversationsScreen();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Conversations'),
      ),
      body: StreamBuilder<QuerySnapshot>(
        stream: Provider.of<ChatStateProvider>(context, listen: false).getUserConversations(userId),
        builder: (context, snapshot) {
          if (snapshot.connectionState == ConnectionState.waiting) {
            return CircularProgressIndicator();
          } else if (!snapshot.hasData || snapshot.data!.docs.isEmpty) {
            return Text("No Conversations");
          } else {
            return ListView.builder(
              itemCount: snapshot.data!.docs.length,
              itemBuilder: (context, index) {
                var conversation = snapshot.data!.docs[index];
                var participants = (conversation['participants'] as List<dynamic>).map((item) => item.toString()).toList();

                String otherUserId = participants.firstWhere((id) => id != userId);
                return FutureBuilder<Map<String, dynamic>>(
                  future: AuthService().fetchOtherUserSettings(userid: otherUserId),
                  builder: (context, userSnapshot) {
                    if (userSnapshot.connectionState == ConnectionState.waiting) {
                      return ListTile(title: Text('Loading...'));
                    } else if (userSnapshot.hasData) {
                      return ListTile(
                        title: Text('Conversation with ${userSnapshot.data!['name']}'), // assuming the profile has a 'name' field
                        onTap: () {
                          Navigator.of(context).push(MaterialPageRoute(
                            builder: (context) => ChatScreen(
                              conversationId: conversation.id,
                              userId: userId,
                            ),
                          ));
                        },
                      );
                    } else {
                      return ListTile(title: Text('Error loading user.'));
                    }
                  },
                );
              },
            );
          }
        },
      ),
    );
  }
}
