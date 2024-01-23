// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'users.dart';

// **************************************************************************
// RealmObjectGenerator
// **************************************************************************

class users extends _users with RealmEntity, RealmObjectBase, RealmObject {
  users(
    String id,
    String name,
    int age,
    String email,
    String bio,
    bool profileCompleted,
    String profilePicURL,
  ) {
    RealmObjectBase.set(this, '_id', id);
    RealmObjectBase.set(this, 'name', name);
    RealmObjectBase.set(this, 'age', age);
    RealmObjectBase.set(this, 'email', email);
    RealmObjectBase.set(this, 'bio', bio);
    RealmObjectBase.set(this, 'profileCompleted', profileCompleted);
    RealmObjectBase.set(this, 'profilePicURL', profilePicURL);
  }

  users._();

  @override
  String get id => RealmObjectBase.get<String>(this, '_id') as String;
  @override
  set id(String value) => RealmObjectBase.set(this, '_id', value);

  @override
  String get name => RealmObjectBase.get<String>(this, 'name') as String;
  @override
  set name(String value) => RealmObjectBase.set(this, 'name', value);

  @override
  int get age => RealmObjectBase.get<int>(this, 'age') as int;
  @override
  set age(int value) => RealmObjectBase.set(this, 'age', value);

  @override
  String get email => RealmObjectBase.get<String>(this, 'email') as String;
  @override
  set email(String value) => RealmObjectBase.set(this, 'email', value);

  @override
  String get bio => RealmObjectBase.get<String>(this, 'bio') as String;
  @override
  set bio(String value) => RealmObjectBase.set(this, 'bio', value);

  @override
  bool get profileCompleted =>
      RealmObjectBase.get<bool>(this, 'profileCompleted') as bool;
  @override
  set profileCompleted(bool value) =>
      RealmObjectBase.set(this, 'profileCompleted', value);

  @override
  String get profilePicURL =>
      RealmObjectBase.get<String>(this, 'profilePicURL') as String;
  @override
  set profilePicURL(String value) =>
      RealmObjectBase.set(this, 'profilePicURL', value);

  @override
  Stream<RealmObjectChanges<users>> get changes =>
      RealmObjectBase.getChanges<users>(this);

  @override
  users freeze() => RealmObjectBase.freezeObject<users>(this);

  static SchemaObject get schema => _schema ??= _initSchema();
  static SchemaObject? _schema;
  static SchemaObject _initSchema() {
    RealmObjectBase.registerFactory(users._);
    return const SchemaObject(ObjectType.realmObject, users, 'users', [
      SchemaProperty('id', RealmPropertyType.string,
          mapTo: '_id', primaryKey: true),
      SchemaProperty('name', RealmPropertyType.string),
      SchemaProperty('age', RealmPropertyType.int),
      SchemaProperty('email', RealmPropertyType.string),
      SchemaProperty('bio', RealmPropertyType.string),
      SchemaProperty('profileCompleted', RealmPropertyType.bool),
      SchemaProperty('profilePicURL', RealmPropertyType.string),
    ]);
  }
}
