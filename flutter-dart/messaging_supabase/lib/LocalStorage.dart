import 'package:shared_preferences/shared_preferences.dart';

import 'ChatModels.dart';
import 'UserModel.dart';

import 'dart:convert';

class LocalStorage {
  static const String KEY_PROFILES = "cached_profiles";
  static const String KEY_MESSAGES = "cached_messages";

  static Future<void> saveMessages(List<Message> messages) async {
    final prefs = await SharedPreferences.getInstance();
    final List<String> strMessages = messages.map((m) => json.encode(m.toJson())).toList();
    await prefs.setStringList(KEY_MESSAGES, strMessages);
  }
  static Future<List<Message>> loadMessages() async {
    final prefs = await SharedPreferences.getInstance();
    final List<String>? strMessages = prefs.getStringList(KEY_MESSAGES);

    if (strMessages != null && strMessages.isNotEmpty) {
      return strMessages.map((s) => Message.fromJson(json.decode(s))).toList();
    } else {
      return [];
    }
  }
  static Future<void> clearMessages() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove(KEY_MESSAGES);
  }

  static Future<void> saveProfiles(List<UserModel> profiles) async {
    final prefs = await SharedPreferences.getInstance();
    final List<String> strProfiles = profiles.map((p) => json.encode(p.toJson())).toList();
    await prefs.setStringList(KEY_PROFILES, strProfiles);
  }

  static Future<List<UserModel>> loadProfiles() async {
    final prefs = await SharedPreferences.getInstance();
    final List<String>? strProfiles = prefs.getStringList(KEY_PROFILES);

    if (strProfiles != null && strProfiles.isNotEmpty) {
      return strProfiles.map((s) => UserModel.fromJson(json.decode(s))).toList();
    } else {
      return [];
    }
  }

  static Future<void> clearProfiles() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.remove(KEY_PROFILES);
  }
}
