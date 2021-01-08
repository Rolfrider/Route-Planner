import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:route_planner/locator.dart';
import 'package:route_planner/model/point.dart';
import 'package:route_planner/planner.dart';

class MapModel extends ChangeNotifier {
  Locator _locator = Locator();

  LatLng _currentPosition;
  Set<LatLng> _points = {};

  Set<Marker> _markers = {};
  Set<Marker> get markers => _markers;

  Polyline _polyline;
  Set<Polyline> get polyline => _polyline != null ? {_polyline} : null;

  getCurrentLocation() async {
    await _locator.getCurrentPosition().then((position) {
      _currentPosition = position;
    });
  }

  _addLine(List<LatLng> points) {
    _polyline = Polyline(
        polylineId: PolylineId("Route"),
        color: Colors.red,
        width: 3,
        points: points);
    notifyListeners();
  }

  addMarker(LatLng point) {
    _points.add(point);
    _markers.add(Marker(
      markerId: MarkerId(point.toString()),
      position: point,
      infoWindow: InfoWindow(
        title: 'Stop', //TODO: Maybe add address or sth
      ),
    ));
    notifyListeners();
  }

  findRoute() async {
    final points = [_currentPosition] + _points.toList();
    final route =
        await routeFor(points.map((e) => Point.fromLatLong(e)).toList());
    _addLine(route.map((e) => e.toLatLong()));
  }
}
