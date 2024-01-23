import 'package:flutter/cupertino.dart';
import 'package:realm/realm.dart';
part 'usersn.g.dart';

// NOTE: These Realm models are private and therefore should be copied into the same .dart file.

@RealmModel()
@MapTo('users')
class _Users {
  @PrimaryKey()
  @MapTo('_id')
  late String id;
  int? age;
  String? bio;
  String? email;
  String? name;
  bool? profileCompleted;
  String? profilePicURL;
}