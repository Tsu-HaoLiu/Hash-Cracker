using System;
using Xunit;

using static HashBuster;

namespace TDD.xUnit.net.Client  {

    public class UnitTest1 {

        [Fact]
        public void WordlistHashTest() {
            string hash = "b109f3bbbc244eb82441917ed06d618b9008dd09b3befd1b5e07394c706a8bb980b1d7785e5976ec049b46df5f1326af5a2ea6d103fd07c95385ffab0cacbc86";
            string hashType = "sha512";
            string fileName = "../../../Wordlist.txt";

            Assert.Equal("password", WordlistHash(hash, hashType, fileName));

            hashType = "UnknownHash";
            var ex = Record.Exception(() => {
                WordlistHash(hash, hashType, fileName);
            });
            Assert.NotNull(ex);
            Assert.IsType<ArgumentException>(ex);

            // Assert.Throws<ArgumentException>(() => {
            //     WordlistHash(hash, hashType, fileName);
            // });
        }

        [Fact]
        public void test2() {
            string hash = "3e52b22ebfaa4ecd02fe6e4d8fecf9f0";
            string hashType = "md5";
            int minLength = 3;
            int maxLength = 5;

            Assert.Equal("c@t$", BruteforceHash(hash, hashType, minLength, maxLength));

            maxLength = 3;
            Assert.Empty(BruteforceHash(hash, hashType, minLength, maxLength));

        }
    }
}

