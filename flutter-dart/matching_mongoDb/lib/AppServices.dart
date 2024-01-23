import 'package:flutter/material.dart';
import 'package:realm/realm.dart';
import 'package:matching2/UserProfiles.dart';
class AppServices with ChangeNotifier {
 // String id;
 // Uri baseUrl;
  //App app;
  User? currentUser;
  late Realm users_db;
  final app = App(AppConfiguration('matching-2-svnnk'));
  //AppServices(this.id, this.baseUrl)
  //    : app = App(AppConfiguration(id, baseUrl: baseUrl));

  AppServices() {
    initUsersDb();
  }

  Future<void> initUsersDb() async {
    // Check if the currentUser object is not null
    if (currentUser != null) {
      // Open a synced realm with Flexible Sync for the user profile collection
      users_db = Realm(Configuration.flexibleSync(currentUser!, [UserProfiles.schema]));
      users_db.subscriptions.update((mutableSubscriptions) {
        mutableSubscriptions.add(users_db.query<UserProfiles>(r'_id == $0', [currentUser?.id]));
      });
      // Sync all subscriptions
      await users_db.subscriptions.waitForSynchronization();
    } else {
      // Do something else
    }
  }

  Future<User> logInUserEmailPassword({required String email, required String password}) async {
    User loggedInUser = await app.logIn(Credentials.emailPassword(email, password));
    currentUser = loggedInUser;
    // Initialize the users_db variable after logging in
    await initUsersDb();

    notifyListeners();
    return loggedInUser;
  }

  Future<User> registerUserEmailPassword({required String email, required String password}) async {
    EmailPasswordAuthProvider authProvider = EmailPasswordAuthProvider(app);
    await authProvider.registerUser(email, password);
    User loggedInUser = await app.logIn(Credentials.emailPassword(email, password));
    currentUser = loggedInUser;
    // Initialize the users_db variable after logging in
    await initUsersDb();

    users_db.write(() {
      users_db.add(UserProfiles(loggedInUser.id, email: email));
    });

    notifyListeners();
    return loggedInUser;
  }

  Future<void> logOut() async {
    await currentUser?.logOut();
    currentUser = null;
    notifyListeners();
  }
}
