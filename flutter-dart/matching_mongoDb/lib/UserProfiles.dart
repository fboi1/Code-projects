import 'package:realm/realm.dart';

part 'UserProfiles.g.dart';
@RealmModel()
class _UserProfiles {
  @MapTo('_id')
  @PrimaryKey()
  late String id;
  int? age;
  String? bio;
  String? email;
  String? name;
  bool? profileCompleted;
  String? profilePicURL;
  String? gender;
  int? swipesCount;
}