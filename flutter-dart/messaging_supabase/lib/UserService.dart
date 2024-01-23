import 'dart:math';

import 'package:supabase_flutter/supabase_flutter.dart' hide User, Provider;
import 'UserModel.dart';


class UserService {
  final supabase = Supabase.instance.client;
  Future<List<UserModel>> getUserProfiles(int currentUserAge, [String? lastId]) async {
    final int ageLimit = 18;
    final int batchSize = 5;  // Number of profiles to fetch in each batch
    Random random = Random ();
    int randomnumber = random.nextInt (50) + 1;

    String filterColumn = currentUserAge < ageLimit ? "lt" : "gte";
    try {
// Calculate the date 3 weeks ago from now
      DateTime threeWeeksAgo = DateTime.now().subtract(Duration(days: 21));

      // Manually format the DateTime object to a String in the 'yyyy-MM-dd' format
      String threeWeeksAgoStr = '${threeWeeksAgo.year}-${threeWeeksAgo.month.toString().padLeft(2, '0')}-${threeWeeksAgo.day.toString().padLeft(2, '0')}';

      final response = await supabase
        .from('profiles')
        .select()
        .filter('age', filterColumn, ageLimit)
        .filter('profilecompleted', 'eq', true)
        .filter('randomnum', 'lt', randomnumber)
        //.filter('lastonline', 'gte', threeWeeksAgoStr)
        .order('age')
        .limit(batchSize);



    return (response as List).map((e) => UserModel.fromJson(e)).toList();
    } catch (error) {
      throw error;

    }
  }
}

