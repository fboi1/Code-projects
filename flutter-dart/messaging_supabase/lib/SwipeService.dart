
import 'package:supabase_flutter/supabase_flutter.dart' hide User, Provider;
class SwipeService {
  final supabase = Supabase.instance.client;
  static const int BATCH_SIZE = 8;
  int swipescount = 0;

  Future<void> createSwipe(String swiper_id, String swipee_id, bool liked) async {
    await supabase
        .from('swipes')
        .insert({
      'swiper_id': swiper_id,
      'swipee_id': swipee_id,
      'liked': liked,
      'timestamp': DateTime.now().toIso8601String(),
    });
  }

  Future<void> incrementswipescount(String userId) async {
    if (swipescount >= BATCH_SIZE) {
      await writeswipescountToSupabase(userId, swipescount);
      swipescount = 0;
    } else {
      swipescount++;
    }
  }

  Future<void> writeswipescountToSupabase(String userId, int count) async {
    await supabase
        .from('profiles')
        .update({'swipescount': count})
        .eq('userid', userId);
  }
}

