using CSItertools.Collections;

namespace CSItertools {
    public sealed class Itertools {
        public IEnumerable<T[]> Product<T>(params IEnumerable<T>[] iterables) {
            var result1 = new List<CustomArray<T>> { new CustomArray<T>() };
            var result2 = new List<CustomArray<T>>();

            foreach (var iterable in iterables) {
                foreach (var x in result1)
                    foreach (var y in iterable)
                        result2.Add(x + new CustomArray<T>(y));

                result1 = new List<CustomArray<T>>(result2);
                result2 = new List<CustomArray<T>>();
            }

            foreach (var r in result1)
                yield return r;
        }

        public IEnumerable<T[]> Product<T>(IEnumerable<T> iterable, int repeat) {
            var iterables = new IEnumerable<T>[repeat];

            for (int i = 0; i < repeat; i++)
                iterables[i] = new List<T>(iterable);

            foreach (T[] item in Product(iterables))
                yield return item;
        }
    }
}