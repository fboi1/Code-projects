// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'UserProfiles.dart';

// **************************************************************************
// RealmObjectGenerator
// **************************************************************************

class UserProfiles extends _UserProfiles
    with RealmEntity, RealmObjectBase, RealmObject {
  UserProfiles(
    String id, {
    int? age,
    String? bio,
    String? email,
    String? name,
    bool? profileCompleted,
    String? profilePicURL,
    String? gender,
    int? swipesCount,
  }) {
    RealmObjectBase.set(this, '_id', id);
    RealmObjectBase.set(this, 'age', age);
    RealmObjectBase.set(this, 'bio', bio);
    RealmObjectBase.set(this, 'email', email);
    RealmObjectBase.set(this, 'name', name);
    RealmObjectBase.set(this, 'profileCompleted', profileCompleted);
    RealmObjectBase.set(this, 'profilePicURL', profilePicURL);
    RealmObjectBase.set(this, 'gender', gender);
    RealmObjectBase.set(this, 'swipesCount', swipesCount);
  }

  UserProfiles._();

  @override
  String get id => RealmObjectBase.get<String>(this, '_id') as String;
  @override
  set id(String value) => RealmObjectBase.set(this, '_id', value);

  @override
  int? get age => RealmObjectBase.get<int>(this, 'age') as int?;
  @override
  set age(int? value) => RealmObjectBase.set(this, 'age', value);

  @override
  String? get bio => RealmObjectBase.get<String>(this, 'bio') as String?;
  @override
  set bio(String? value) => RealmObjectBase.set(this, 'bio', value);

  @override
  String? get email => RealmObjectBase.get<String>(this, 'email') as String?;
  @override
  set email(String? value) => RealmObjectBase.set(this, 'email', value);

  @override
  String? get name => RealmObjectBase.get<String>(this, 'name') as String?;
  @override
  set name(String? value) => RealmObjectBase.set(this, 'name', value);

  @override
  bool? get profileCompleted =>
      RealmObjectBase.get<bool>(this, 'profileCompleted') as bool?;
  @override
  set profileCompleted(bool? value) =>
      RealmObjectBase.set(this, 'profileCompleted', value);

  @override
  String? get profilePicURL =>
      RealmObjectBase.get<String>(this, 'profilePicURL') as String?;
  @override
  set profilePicURL(String? value) =>
      RealmObjectBase.set(this, 'profilePicURL', value);

  @override
  String? get gender => RealmObjectBase.get<String>(this, 'gender') as String?;
  @override
  set gender(String? value) => RealmObjectBase.set(this, 'gender', value);

  @override
  int? get swipesCount => RealmObjectBase.get<int>(this, 'swipesCount') as int?;
  @override
  set swipesCount(int? value) =>
      RealmObjectBase.set(this, 'swipesCount', value);

  @override
  Stream<RealmObjectChanges<UserProfiles>> get changes =>
      RealmObjectBase.getChanges<UserProfiles>(this);

  @override
  UserProfiles freeze() => RealmObjectBase.freezeObject<UserProfiles>(this);

  static SchemaObject get schema => _schema ??= _initSchema();
  static SchemaObject? _schema;
  static SchemaObject _initSchema() {
    RealmObjectBase.registerFactory(UserProfiles._);
    return const SchemaObject(
        ObjectType.realmObject, UserProfiles, 'UserProfiles', [
      SchemaProperty('id', RealmPropertyType.string,
          mapTo: '_id', primaryKey: true),
      SchemaProperty('age', RealmPropertyType.int, optional: true),
      SchemaProperty('bio', RealmPropertyType.string, optional: true),
      SchemaProperty('email', RealmPropertyType.string, optional: true),
      SchemaProperty('name', RealmPropertyType.string, optional: true),
      SchemaProperty('profileCompleted', RealmPropertyType.bool,
          optional: true),
      SchemaProperty('profilePicURL', RealmPropertyType.string, optional: true),
      SchemaProperty('gender', RealmPropertyType.string, optional: true),
      SchemaProperty('swipesCount', RealmPropertyType.int, optional: true),
    ]);
  }
}
