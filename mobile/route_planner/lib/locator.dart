import 'package:geolocator/geolocator.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';

class Locator {
  final _geloccator = Geolocator();

  Future<LatLng> getCurrentPosition() async {
    return await _geloccator
        .getCurrentPosition(desiredAccuracy: LocationAccuracy.high)
        .then((position) => LatLng(position.latitude, position.longitude))
        .catchError((e) {
      print(e);
    });
  }
}
