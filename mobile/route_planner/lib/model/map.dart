import 'package:flutter/foundation.dart';
import 'package:flutter_polyline_points/flutter_polyline_points.dart';
import 'package:geolocator/geolocator.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:route_planner/locator.dart';

class MapModel extends ChangeNotifier {
  Locator _locator = Locator();

  LatLng _currentPosition;
  Set<LatLng> _points = {};
  Set<Marker> _markers = {};
  Set<Marker> get markers => _markers;

  getCurrentLocation() async {
    await _locator.getCurrentPosition().then((position) {
      _currentPosition = position;
    });
  }

  addMarker(LatLng point) {
    _points.add(point);
    _markers.add(Marker(
      markerId: MarkerId(point.toString()),
      position: point,
      infoWindow: InfoWindow(
        title: 'Stop',
      ),
    ));
    notifyListeners();
  }
}
