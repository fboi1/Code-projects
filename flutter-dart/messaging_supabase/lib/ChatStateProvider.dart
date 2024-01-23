import 'dart:async';

import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:flutter/material.dart';
import 'package:messaging_supabase/ChatModels.dart';


class ChatStateProvider with ChangeNotifier {
  final conversationsCollection = FirebaseFirestore.instance.collection('conversations');
  DocumentSnapshot? lastDocumentSnapshot; // for pagination

  // Retrieve conversations for a user
  Stream<QuerySnapshot> getUserConversations(String userId) {
    return conversationsCollection.where('participants', arrayContains: userId).snapshots();
  }

  Stream<QuerySnapshot> getMessagesFromConversation(String conversationId) { return conversationsCollection.doc(conversationId).collection('messages').orderBy('timestamp', descending: true).limit(20).snapshots(); }
//

  final int _messagesLimit = 20;
  DocumentSnapshot? _lastDocument; // Last document for pagination

  // New method to fetch older messages
  Future<List<DocumentSnapshot>> fetchOldMessages(String conversationId, DocumentSnapshot? lastMessage) async {
    Query query = conversationsCollection
        .doc(conversationId)
        .collection('messages')
        .orderBy('timestamp', descending: true)
        .limit(10);

    if (lastMessage != null) {
      query = query.startAfterDocument(lastMessage);
    }

    QuerySnapshot querySnapshot = await query.get();
    return querySnapshot.docs;
  }
  StreamController<List<DocumentSnapshot>> _messagesController = StreamController<List<DocumentSnapshot>>.broadcast();

  // Existing code...

  Stream<List<DocumentSnapshot>> get realTimeMessages => _messagesController.stream;

  void listenToRealTimeMessages(String conversationId) {
    conversationsCollection
        .doc(conversationId)
        .collection('messages')
        .orderBy('timestamp', descending: true)
        .limit(10)
        .snapshots()
        .listen((snapshot) {
      if (snapshot.docs.isNotEmpty) {
        _messagesController.add(snapshot.docs);
      }
    });
  }

  //
  Future<void> addMessage(String conversationId, String senderId, String content) async {
    DocumentReference messageRef = await conversationsCollection.doc(conversationId).collection('messages').add({
      'timestamp': Timestamp.now(),
      'sender_id': senderId,
      'content': content,
      'message_type': 0, // Assuming 0 is a text message
      'is_read': 0, // Assuming 0 means unread
      // 'conversation_id': conversationId, // If you decide to keep this field
    });

    // Update last_message_id in the conversation
    await conversationsCollection.doc(conversationId).update({
      'last_message_id': messageRef,
      'updated_at': Timestamp.now(),
    });
  }
  Future<void> markMessagesAsRead(String conversationId) async {
    // Get the last 20 unread messages from the conversation (or however many you want to mark at once)
    QuerySnapshot unreadMessages = await conversationsCollection.doc(conversationId).collection('messages').where('is_read', isEqualTo: 0).limit(20).get();

    for (DocumentSnapshot message in unreadMessages.docs) {
      message.reference.update({
        'is_read': 1, // Assuming 1 means read
      });
    }
  }


// ... [Other methods we defined previously]
}



