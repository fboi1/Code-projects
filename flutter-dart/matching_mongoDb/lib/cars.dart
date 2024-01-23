import 'package:realm/realm.dart';

part 'cars.g.dart';

@RealmModel()
class _Cars {
  @MapTo('_id')
  @PrimaryKey()
  late ObjectId id;
  bool isComplete = false;
  late String summary;
}