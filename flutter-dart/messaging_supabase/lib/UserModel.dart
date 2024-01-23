class UserModel {
  final String id;
  final String name;
  final String bio;
  final int age;
  final String profilepicurl;

  UserModel({
    required this.id,
    required this.name,
    required this.bio,
    required this.age,
    required this.profilepicurl,
  });

  // Converts a Map into a UserModel
  factory UserModel.fromJson(Map<String, dynamic> json) {
    return UserModel(
      id: json['userid'],
      name: json['name'] ?? '',
      bio: json['bio'] ?? '',
      age: json['age'] ?? 0,
      profilepicurl: json['profilepicurl'] ?? '',
    );
  }
  Map<String, dynamic> toJson() {
    return {
      'userid': this.id,
      'name': this.name,
      'bio': this.bio,
      'age': this.age,
      'profilepicurl': this.profilepicurl,
    };}
}


