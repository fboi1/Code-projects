import 'package:provider/provider.dart';
import 'package:flutter/material.dart';
// models/conversation.dart
class Conversation {
  final String id;
  final String user1Id;
  final String user2Id;
  // add other fields

  Conversation({required this.id, required this.user1Id, required this.user2Id});
}

// models/message.dart
class Message {
  final int id;
  final String conversationId;
  final int senderId;
  final String content;
  //final date timestamp;
  // add other fields

  Message({required this.id, required this.conversationId, required this.senderId, required this.content});
  Map<String, dynamic> toJson() {
    return {
      'id': id,
      'conversationId': conversationId,
      'senderId': senderId,
      'content': content,
      // add other fields as needed
    };
  }
  factory Message.fromJson(Map<String, dynamic> json) {
    return Message(
      id: json['id'],
      conversationId: json['conversationId'],
      senderId: json['senderId'],
      content: json['content'],
      // initialize other fields as necessary
    );
  }
}

// providers/chat_provider.dart
class ChatProvider with ChangeNotifier {
  List<Conversation> _conversations = [];
  List<Message> _messages = [];

  List<Conversation> get conversations => _conversations;
  List<Message> get messages => _messages;

  void setConversations(List<Conversation> conversations) {
    _conversations = conversations;
    notifyListeners();
  }

  void setMessages(List<Message> messages) {
    _messages = messages;
    notifyListeners();
  }
}
