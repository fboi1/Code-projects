// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'cars.dart';

// **************************************************************************
// RealmObjectGenerator
// **************************************************************************

class Cars extends _Cars with RealmEntity, RealmObjectBase, RealmObject {
  static var _defaultsSet = false;

  Cars(
    ObjectId id,
    String summary, {
    bool isComplete = false,
  }) {
    if (!_defaultsSet) {
      _defaultsSet = RealmObjectBase.setDefaults<Cars>({
        'isComplete': false,
      });
    }
    RealmObjectBase.set(this, '_id', id);
    RealmObjectBase.set(this, 'isComplete', isComplete);
    RealmObjectBase.set(this, 'summary', summary);
  }

  Cars._();

  @override
  ObjectId get id => RealmObjectBase.get<ObjectId>(this, '_id') as ObjectId;
  @override
  set id(ObjectId value) => RealmObjectBase.set(this, '_id', value);

  @override
  bool get isComplete => RealmObjectBase.get<bool>(this, 'isComplete') as bool;
  @override
  set isComplete(bool value) => RealmObjectBase.set(this, 'isComplete', value);

  @override
  String get summary => RealmObjectBase.get<String>(this, 'summary') as String;
  @override
  set summary(String value) => RealmObjectBase.set(this, 'summary', value);

  @override
  Stream<RealmObjectChanges<Cars>> get changes =>
      RealmObjectBase.getChanges<Cars>(this);

  @override
  Cars freeze() => RealmObjectBase.freezeObject<Cars>(this);

  static SchemaObject get schema => _schema ??= _initSchema();
  static SchemaObject? _schema;
  static SchemaObject _initSchema() {
    RealmObjectBase.registerFactory(Cars._);
    return const SchemaObject(ObjectType.realmObject, Cars, 'Cars', [
      SchemaProperty('id', RealmPropertyType.objectid,
          mapTo: '_id', primaryKey: true),
      SchemaProperty('isComplete', RealmPropertyType.bool),
      SchemaProperty('summary', RealmPropertyType.string),
    ]);
  }
}
