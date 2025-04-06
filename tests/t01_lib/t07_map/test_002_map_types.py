"""
@pyne
"""
from pynecore.lib import script, log, bar_index, map, color


@script.indicator(title="Map Types", shorttitle="map_types")
def main():
    if bar_index == 0:
        # Test with different key and value types
        map_int_keys = map.new()
        map.put(map_int_keys, 1, "one")
        map.put(map_int_keys, 2, "two")
        map.put(map_int_keys, 3, "three")

        # Log map contents
        log.info("map_int_keys size: {0}", map.size(map_int_keys))
        log.info("map_int_keys[1]: {0}", map.get(map_int_keys, 1))
        log.info("map_int_keys[2]: {0}", map.get(map_int_keys, 2))
        log.info("map_int_keys[3]: {0}", map.get(map_int_keys, 3))

        # Test with float values
        map_float_vals = map.new()
        map.put(map_float_vals, "pi", 3.14159)
        map.put(map_float_vals, "e", 2.71828)
        map.put(map_float_vals, "sqrt2", 1.41421)

        # Log float map contents
        log.info("map_float_vals size: {0}", map.size(map_float_vals))
        log.info("map_float_vals['pi']: {0,number,#.#####}", map.get(map_float_vals, "pi"))
        log.info("map_float_vals['e']: {0,number,#.#####}", map.get(map_float_vals, "e"))
        log.info("map_float_vals['sqrt2']: {0,number,#.#####}", map.get(map_float_vals, "sqrt2"))

        # Test with boolean values
        map_bool_vals = map.new()
        map.put(map_bool_vals, "isTrue", True)
        map.put(map_bool_vals, "isFalse", False)

        # Log boolean map contents
        log.info("map_bool_vals size: {0}", map.size(map_bool_vals))
        log.info("map_bool_vals[isTrue]: {0}", map.get(map_bool_vals, "isTrue"))
        log.info("map_bool_vals[isFalse]: {0}", map.get(map_bool_vals, "isFalse"))

        # Test with color values
        map_color_vals = map.new()
        map.put(map_color_vals, "red", color.red)
        map.put(map_color_vals, "green", color.green)
        map.put(map_color_vals, "blue", color.blue)

        # Log color comparison
        log.info("map_color_vals[red] == color.red: {0}", map.get(map_color_vals, "red") == color.red)
        log.info("map_color_vals[green] == color.green: {0}", map.get(map_color_vals, "green") == color.green)
        log.info("map_color_vals[blue] == color.blue: {0}", map.get(map_color_vals, "blue") == color.blue)

        # Test with nested maps
        inner_map1 = map.new()
        map.put(inner_map1, "a", 1)
        map.put(inner_map1, "b", 2)

        inner_map2 = map.new()
        map.put(inner_map2, "c", 3)
        map.put(inner_map2, "d", 4)

        outer_map = map.new()
        map.put(outer_map, "map1", inner_map1)
        map.put(outer_map, "map2", inner_map2)

        # Log nested map information
        outer_keys = map.keys(outer_map)
        log.info("outer_map keys: {0}", outer_keys)

        inner_map_from_outer = map.get(outer_map, "map1")
        log.info("inner_map1 from outer - a: {0}", map.get(inner_map_from_outer, "a"))
        log.info("inner_map1 from outer - b: {0}", map.get(inner_map_from_outer, "b"))

        # Test with arrays as values
        arr1 = []
        arr1.append(10)
        arr1.append(20)
        arr1.append(30)

        map_with_arrays = map.new()
        map.put(map_with_arrays, "integers", arr1)

        # Log array in map information
        map_with_arrays_keys = map.keys(map_with_arrays)
        log.info("map_with_arrays keys: {0}", map_with_arrays_keys)

        array_from_map = map.get(map_with_arrays, "integers")
        log.info("array from map size: {0}", len(array_from_map))
        log.info("array from map[0]: {0}", array_from_map[0])
        log.info("array from map[1]: {0}", array_from_map[1])
        log.info("array from map[2]: {0}", array_from_map[2])


def __test_map_types__(runner, dummy_ohlcv_iter, file_reader, log_comparator):
    """ Types """
    tv_log_out = file_reader(subdir="data", suffix=".txt")
    run_iter = runner(dummy_ohlcv_iter).run_iter()
    with log_comparator(tv_log_out):
        next(run_iter)
