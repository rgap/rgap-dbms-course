### Geospatial Model — Realistic Location Collection

This example shows how to store and index geographic location data using the GeoJSON `Point` format. Each document represents a place and includes its coordinates for geospatial operations.

🧱 **Fields**:

- `_id` _(string)_: Unique identifier.
- `name` _(string)_: Name of the place or business.
- `type` _(string)_: Type or category of the place (e.g., cafe, park, coworking).
- `location` _(object)_:
  - `type`: Always `"Point"` for a single geographic coordinate.
  - `coordinates`: An array `[longitude, latitude]` in decimal degrees.

📌 **Use Cases**:

- Suitable for apps that need to locate nearby points of interest.
- Useful for mapping services, delivery systems, or any location-based features.
- Ideal for spatial indexing and proximity searches.

✅ **Advantages**:

- Supports advanced spatial queries with MongoDB's 2dsphere index.
- Compatible with mapping tools and GeoJSON standards.
- Efficient for radius, bounding box, and route-based queries.

🚫 **Limitations**:

- Requires specific format and indexing for geospatial queries.
- Coordinates must follow strict `[longitude, latitude]` order.
- Only supports WGS 84 coordinate reference system.
