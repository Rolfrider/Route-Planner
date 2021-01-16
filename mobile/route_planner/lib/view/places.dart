import 'package:flutter/material.dart';
import 'package:flutter/widgets.dart';

class PlacesList extends StatefulWidget {
  PlacesList({Key key, this.places, this.onPlaceTap, this.selectedIndex})
      : super(key: key);

  final List<String> places;
  final Function(int) onPlaceTap;
  final int selectedIndex;

  @override
  _PlacesListState createState() => _PlacesListState();
}

class _PlacesListState extends State<PlacesList> {
  @override
  Widget build(BuildContext context) {
    return ListView.separated(
      itemCount: widget.places.length,
      itemBuilder: placeCellBuilder,
      padding: EdgeInsets.symmetric(horizontal: 8),
      scrollDirection: Axis.horizontal,
      separatorBuilder: (BuildContext context, int index) => Container(
        width: 8,
      ),
    );
  }

  Widget placeCellBuilder(BuildContext context, int index) {
    return ClipRRect(
        borderRadius: BorderRadius.circular(24),
        child: GestureDetector(
          child: Container(
            alignment: Alignment.center,
            padding: EdgeInsets.symmetric(vertical: 4, horizontal: 8),
            child: Text(
              widget.places[index],
              style: TextStyle(color: Colors.white),
            ),
            color: _isSelected(index) ? Colors.deepPurple : Colors.blue,
          ),
          onTap: () => widget.onPlaceTap(index),
        ));
  }

  bool _isSelected(int index) => widget.selectedIndex == index;
}
