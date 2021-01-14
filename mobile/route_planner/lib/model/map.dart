import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:route_planner/model/point.dart';
import 'package:route_planner/service/locator.dart';
import 'package:route_planner/service/planner.dart';

class MapModel extends ChangeNotifier {
  static final bounds = LatLngBounds(
      northeast: LatLng(52.368153, 21.271151),
      southwest: LatLng(52.097851, 20.851688));

  Locator _locator = Locator();

  LatLng _currentPosition;
  Set<LatLng> _points = {};

  bool _isLoading = true;
  bool get isLoading => _isLoading;

  Set<Marker> _markers = {};
  Set<Marker> get markers => _markers;

  List<String> get places => _markers.map((e) => e.infoWindow.title).toList();
  Marker selectedMarker;
  int get selectedPlace => _markers.toList().indexOf(selectedMarker);
  set selectedPlace(int index) {
    selectedMarker = _markers.toList()[index];
    notifyListeners();
  }

  Polyline _polyline;
  Set<Polyline> get polyline => _polyline != null ? {_polyline} : null;

  getCurrentLocation() async => doWithLoading(_getCurrentLocation);

  _getCurrentLocation() async {
    await _locator.getCurrentPosition().then((position) {
      _currentPosition = position;
    });
  }

  removePlace() {
    _markers.remove(selectedMarker);
    selectedMarker = null;
    notifyListeners();
  }

  _addLine(List<LatLng> points) {
    _polyline = Polyline(
        polylineId: PolylineId("Route"),
        color: Colors.red,
        width: 3,
        points: points);
    notifyListeners();
  }

  addMarker(LatLng point) => doWithLoading(() => _addMarker(point));

  _addMarker(LatLng point) async {
    if (!bounds.contains(point)) {
      return;
    }
    _points.add(point);
    _markers.add(Marker(
      markerId: MarkerId(point.toString()),
      position: point,
      infoWindow: InfoWindow(
        title: await _locator.getPlaceName(point),
      ),
    ));
  }

  findRoute() async => doWithLoading(_findRoute);

  _findRoute() async {
    final points = [_currentPosition] + _points.toList();
    final route =
        await routeFor(points.map((e) => Point.fromLatLong(e)).toList());
    _addLine(route.map((e) => e.toLatLong()).toList());
  }

  // ignore: non_constant_identifier_names
  doWithLoading(Function) async {
    _isLoading = true;
    notifyListeners();
    await Function();
    _isLoading = false;
    notifyListeners();
  }
}
