import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:flutter_polyline_points/flutter_polyline_points.dart';
import 'package:geolocator/geolocator.dart';
import 'package:google_maps_flutter/google_maps_flutter.dart';
import 'package:route_planner/model/map.dart';
import 'package:route_planner/view/places.dart';

class MapView extends StatefulWidget {
  @override
  _MapViewState createState() => _MapViewState();
}

class _MapViewState extends State<MapView> {
  CameraPosition _initialLocation =
      CameraPosition(target: LatLng(52.237049, 21.017532), zoom: 10);

  final _bounds = CameraTargetBounds(MapModel.bounds);

  @override
  void initState() {
    super.initState();
  }

  MapModel model;

  @override
  Widget build(BuildContext context) {
    model = context.watch<MapModel>();
    var height = MediaQuery.of(context).size.height;
    var width = MediaQuery.of(context).size.width;

    return Scaffold(
      body: Stack(
        children: <Widget>[
          SafeArea(
              child: Column(
            children: [
              ColoredBox(
                color: Colors.grey[100],
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Container(
                      padding: EdgeInsets.symmetric(vertical: 16),
                      child: Text('Places to visit: ${model.places.length}'),
                    ),
                    if (model.places.isNotEmpty)
                      Container(
                        height: 30,
                        child: PlacesList(
                          places: model.places,
                          selectedIndex: model.selectedPlace,
                          onPlaceTap: (index) => model.selectedPlace = index,
                        ),
                      ),
                    Container(
                      padding: EdgeInsets.only(left: 16, right: 16, bottom: 8),
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          RaisedButton(
                            onPressed: model.selectedMarker != null
                                ? () => model.removePlace()
                                : null,
                            child: Text("Remove place"),
                            color: Colors.blue[200],
                            shape: RoundedRectangleBorder(
                                borderRadius: BorderRadius.circular(16)),
                          ),
                          RaisedButton(
                              onPressed: model.polyline != null
                                  ? () => model.clearMap()
                                  : null,
                              child: Text("Clear route"),
                              color: Colors.blue[200],
                              shape: RoundedRectangleBorder(
                                  borderRadius: BorderRadius.circular(16))),
                          RaisedButton(
                              onPressed: model.markers.isNotEmpty
                                  ? () => model.findRoute()
                                  : null,
                              child: Text("Find route"),
                              color: Colors.blue[200],
                              shape: RoundedRectangleBorder(
                                  borderRadius: BorderRadius.circular(16))),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
              Expanded(
                child: GoogleMap(
                  markers: model.markers,
                  mapToolbarEnabled: false,
                  compassEnabled: false,
                  myLocationEnabled: true,
                  myLocationButtonEnabled: false,
                  mapType: MapType.normal,
                  zoomGesturesEnabled: true,
                  initialCameraPosition: _initialLocation,
                  cameraTargetBounds: _bounds,
                  zoomControlsEnabled: false,
                  polylines: model.polyline,
                  onMapCreated: (GoogleMapController controller) {
                    model.getCurrentLocation();
                  },
                  onTap: model.addMarker,
                ),
              )
            ],
          )),
          if (model.isLoading)
            Container(
              width: width,
              height: height,
              alignment: Alignment.center,
              color: Colors.white60,
              child: CircularProgressIndicator(
                valueColor: AlwaysStoppedAnimation<Color>(Colors.blueGrey),
              ),
            ),
        ],
      ),
    );
  }
}
