import 'package:realm/realm.dart';
part 'users.g.dart';
@RealmModel()
class _users {
  @MapTo('_id')
  @PrimaryKey()
  late String id;
  late String name;
  late int age;
  late String email;
  late String bio;
  late bool profileCompleted;
  late String profilePicURL;

}