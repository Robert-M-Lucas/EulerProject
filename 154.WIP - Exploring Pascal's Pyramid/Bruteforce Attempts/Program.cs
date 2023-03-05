using System;
using System.Collections;
using System.Collections.Generic;

namespace Euler154
{
    class Program
    {
        static void AddToDict(Dictionary<Tuple<long, long, long>, long> dict, Tuple<long, long, long> key, long value)
        {
            if (dict.ContainsKey(key))
            {
                dict[key] += value;
            }
            else
            {
                dict[key] = value;
            }
        }

        static void Main(string[] args)
        {
            Dictionary<Tuple<long, long, long>, long> Coefs = new Dictionary<Tuple<long, long, long>, long>();
            Coefs[new Tuple<long, long, long>(0, 0, 0)] = 1;

            for (long p = 1; p <= 200000; p++)
            {
                Dictionary<Tuple<long, long, long>, long> NewCoefs = new Dictionary<Tuple<long, long, long>, long>();

                foreach (Tuple<long, long, long> coefKey in Coefs.Keys)
                {
                    long current_coef = Coefs[coefKey];
                    AddToDict(NewCoefs, new Tuple<long, long, long>(coefKey.Item1+1, coefKey.Item2, coefKey.Item3), current_coef);
                    AddToDict(NewCoefs, new Tuple<long, long, long>(coefKey.Item1, coefKey.Item2+1, coefKey.Item3), current_coef);
                    AddToDict(NewCoefs, new Tuple<long, long, long>(coefKey.Item1, coefKey.Item2, coefKey.Item3+1), current_coef);
                }

                Coefs = NewCoefs;
                Console.Write(p);
                Console.Write(" ");
                Console.WriteLine(Coefs.Count);
            }

            long total = 0;
            foreach (Tuple<long, long, long> coefKey in Coefs.Keys)
            {
                if (Coefs[coefKey] % 1_000_000_000_000 == 0)
                {
                    total++;
                }
            }
            Console.WriteLine(total);
        }
    }
}
