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

  Future<String> getPlaceName(LatLng position) async {
    return await _geloccator
        .placemarkFromCoordinates(position.latitude, position.longitude)
        .then((value) => _description(value.first))
        .catchError((e) => print(e));
  }

  String _description(Placemark placemark) =>
      [placemark.thoroughfare, placemark.name]
          .toSet()
          .where((element) => element != null && element.isNotEmpty)
          .join(" ");
}
