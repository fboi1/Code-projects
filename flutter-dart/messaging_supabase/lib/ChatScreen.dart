import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

import 'ChatModels.dart';
import 'ChatService.dart';
import 'ChatStateProvider.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

class ChatScreen extends StatefulWidget {
  final String conversationId;
  final String userId;

  ChatScreen({required this.conversationId, required this.userId});

  @override
  _ChatScreenState createState() => _ChatScreenState();
}

class _ChatScreenState extends State<ChatScreen> {
  final TextEditingController _messageController = TextEditingController();
  final ScrollController _scrollController = ScrollController();
  List<DocumentSnapshot> _messages = [];
  DocumentSnapshot? _lastMessage;
  bool _isLoadingOldMessages = false;
  bool _hasMoreMessages = true;

  @override
  void initState() {
    super.initState();
    _scrollController.addListener(_scrollListener);
    _loadInitialMessages();
    Provider.of<ChatStateProvider>(context, listen: false).listenToRealTimeMessages(widget.conversationId);
  }

  void _scrollListener() {
    if (_scrollController.position.atEdge) {
      if (_scrollController.position.pixels == 0 && _hasMoreMessages) {
        print("loading");
        // User has scrolled to the top, load older messages
        _loadOldMessages();
      }
    }
  }

  Future<void> _loadOldMessages() async {
    if (_isLoadingOldMessages) return;

    setState(() {
      _isLoadingOldMessages = true;
    });

    List<DocumentSnapshot> newMessages = await Provider.of<ChatStateProvider>(context, listen: false).fetchOldMessages(widget.conversationId, _lastMessage);

    if (newMessages.isNotEmpty) {
      setState(() {
        _lastMessage = newMessages.last;
        _messages.insertAll(0, newMessages);
      });
    } else {
      setState(() {
        _hasMoreMessages = false;
      });
    }

    setState(() {
      _isLoadingOldMessages = false;
    });
  }



  Future<void> _loadInitialMessages() async {
    List<DocumentSnapshot> messages = await Provider.of<ChatStateProvider>(context, listen: false).fetchOldMessages(widget.conversationId, null);
    setState(() {
      _messages = messages;
      _lastMessage = messages.isNotEmpty ? messages.last : null;
    });
  }

  void _mergeMessages(List<DocumentSnapshot> newMessages) {
    final allMessages = {..._messages, ...newMessages};
    _messages = allMessages.toList()..sort((a, b) => b['timestamp'].compareTo(a['timestamp']));
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Chat'),
      ),
      body: Column(
        children: [
          Expanded(
            child: StreamBuilder<List<DocumentSnapshot>>(
              stream: Provider.of<ChatStateProvider>(context).realTimeMessages,
              builder: (context, snapshot) {
                if (snapshot.connectionState == ConnectionState.waiting && _messages.isEmpty) {
                  return CircularProgressIndicator();
                } else {
                  if (snapshot.hasData) {
                    _mergeMessages(snapshot.data!);
                  }

                  return ListView.builder(
                    controller: _scrollController,
                    reverse: true,
                    itemCount: _messages.length,
                    itemBuilder: (context, index) {
                      var message = _messages[index];
                      bool isSentByMe = message['sender_id'] == widget.userId;

                      return ListTile(
                        title: Text(message['content']),
                        subtitle: Text(message['timestamp'].toDate().toString()),
                        leading: isSentByMe ? null : Icon(Icons.account_circle),
                        trailing: isSentByMe ? Icon(Icons.account_circle) : null,
                      );
                    },
                  );
                }
              },
            ),
          ),
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 8.0, vertical: 4.0),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _messageController,
                    decoration: InputDecoration(hintText: 'Type a message'),
                  ),
                ),
                IconButton(
                  icon: Icon(Icons.send),
                  onPressed: () {
                    if (_messageController.text.isNotEmpty) {
                      Provider.of<ChatStateProvider>(context, listen: false)
                          .addMessage(widget.conversationId, widget.userId, _messageController.text);
                      _messageController.clear();
                    }
                  },
                )
              ],
            ),
          ),
        ],
      ),

    );


  }
  @override
  void dispose() {
    _scrollController.dispose();
    _messageController.dispose();
    super.dispose();
  }

}