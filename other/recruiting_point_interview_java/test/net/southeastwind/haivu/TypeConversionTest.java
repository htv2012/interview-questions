/**
 * @file TypeConversionTest.java
 * Interview Coding for Recruiting Point
 * 2014-06-10
 * @author Hai Vu
 */

package net.southeastwind.haivu;

import org.junit.Test;
import static org.junit.Assert.*;

/**
 * Tests for class TypeConversion
 * @author Hai Vu
 */
public class TypeConversionTest {

    public void performTest(int expected, String s) {
        int actual = TypeConversion.stringToInteger(s);
        assertEquals(expected, actual);
    }
    
    public void performBoundaryTest(int expected) {
        String s = Integer.toString(expected);
        int actual = TypeConversion.stringToInteger(s);
        assertEquals(expected, actual);
    }

    // Tests: Random cases
    @Test public void testRandom_01() { performTest(125, "125"); }
    @Test public void testRandom_02() { performTest(91, "91"); }
    @Test public void testRandom_03() { performTest(3333, "3333"); }
    @Test public void testRandom_04() { performTest(47689, "47689"); }
    @Test public void testRandom_05() { performTest(9876543, "9876543"); }

    // Tests: ssingle digit
    @Test public void testSingleDigit_01() { performTest(1, "1"); }
    @Test public void testSingleDigit_02() { performTest(2, "2"); }
    @Test public void testSingleDigit_03() { performTest(3, "3"); }
    @Test public void testSingleDigit_04() { performTest(4, "4"); }
    @Test public void testSingleDigit_05() { performTest(5, "5"); }
    @Test public void testSingleDigit_06() { performTest(6, "6"); }
    @Test public void testSingleDigit_07() { performTest(7, "7"); }
    @Test public void testSingleDigit_08() { performTest(8, "8"); }
    @Test public void testSingleDigit_09() { performTest(9, "9"); }
    @Test public void testSingleDigit_11() { performTest(-1, "-1"); }
    @Test public void testSingleDigit_12() { performTest(-2, "-2"); }
    @Test public void testSingleDigit_13() { performTest(-3, "-3"); }
    @Test public void testSingleDigit_14() { performTest(-4, "-4"); }
    @Test public void testSingleDigit_15() { performTest(-5, "-5"); }
    @Test public void testSingleDigit_16() { performTest(-6, "-6"); }
    @Test public void testSingleDigit_17() { performTest(-7, "-7"); }
    @Test public void testSingleDigit_18() { performTest(-8, "-8"); }
    @Test public void testSingleDigit_19() { performTest(-9, "-9"); }
    
    // Tests: zeros
    @Test public void testZero_01() { performTest(0, "0"); }
    @Test public void testZero_02() { performTest(0, "-0"); }
    @Test public void testZero_03() { performTest(0, "000"); }
    
    // Tests: with leading zeros
    @Test public void testWithLeadingZeros_01() { performTest(1, "01"); }
    @Test public void testWithLeadingZeros_02() { performTest(2, "002"); }
    @Test public void testWithLeadingZeros_03() { performTest(3, "0003"); }
    @Test public void testWithLeadingZeros_04() { performTest(4, "00004"); }
    
    // Tests: minus sign
    @Test public void testWithMinusSign_01() { performTest(-45, "-45"); }
    @Test public void testWithMinusSign_02() { performTest(-459, "-0459"); }
    @Test public void testWithMinusSign_03() { performTest(-9, "-9"); }
    @Test public void testWithMinusSign_04() { performTest(-9, "-09"); }
    @Test public void testWithMinusSign_05() { performTest(-100, "-100"); }

    // Tests: plus sign
    @Test public void testWithPlusSign_01() { performTest(45, "45"); }
    @Test public void testWithPlusSign_02() { performTest(459, "0459"); }
    @Test public void testWithPlusSign_03() { performTest(9, "9"); }
    @Test public void testWithPlusSign_04() { performTest(9, "09"); }
    @Test public void testWithPlusSign_05() { performTest(100, "100"); }
    
    // Tests: Boundaries: max, min
    @Test public void testBoundary_01() { performBoundaryTest(Integer.MAX_VALUE); }
    @Test public void testBoundary_02() { performBoundaryTest(Integer.MAX_VALUE -  1); }
    @Test public void testBoundary_03() { performBoundaryTest(Integer.MAX_VALUE -  9); }
    @Test public void testBoundary_04() { performBoundaryTest(Integer.MAX_VALUE - 10); }
    @Test public void testBoundary_05() { performBoundaryTest(Integer.MIN_VALUE); }
    @Test public void testBoundary_06() { performBoundaryTest(Integer.MIN_VALUE +  1); }
    @Test public void testBoundary_07() { performBoundaryTest(Integer.MIN_VALUE +  9); }
    @Test public void testBoundary_08() { performBoundaryTest(Integer.MIN_VALUE + 10); }
    
    // Tests: Invalid data, expect exception
    @Test(expected=NumberFormatException.class)
    public void testInvalid_01() { TypeConversion.stringToInteger("x"); }

    @Test(expected=NumberFormatException.class)
    public void testInvalid_02() { TypeConversion.stringToInteger("12k"); }

    @Test(expected=NumberFormatException.class)
    public void testInvalid_03() { TypeConversion.stringToInteger("a8"); }

    @Test(expected=NumberFormatException.class)
    public void testInvalid_04() { TypeConversion.stringToInteger("82 "); }

    @Test(expected=NumberFormatException.class)
    public void testInvalid_05() { TypeConversion.stringToInteger(" 15"); }

    @Test(expected=NumberFormatException.class)
    public void testInvalid_06() { TypeConversion.stringToInteger("--15 "); }

    @Test(expected=NumberFormatException.class)
    public void testInvalid_07() { TypeConversion.stringToInteger("++15 "); }

    @Test(expected=NumberFormatException.class)
    public void testInvalid_08() { TypeConversion.stringToInteger("-+15 "); }

    @Test(expected=NumberFormatException.class)
    public void testInvalid_09() { TypeConversion.stringToInteger("+-15 "); }

    @Test(expected=NumberFormatException.class)
    public void testInvalid_10() { TypeConversion.stringToInteger("15,256"); }

    @Test(expected=NumberFormatException.class)
    public void testInvalid_11() { TypeConversion.stringToInteger("15.256"); }

    @Test(expected=NumberFormatException.class)
    public void testInvalid_12() { TypeConversion.stringToInteger(".2"); }

    @Test(expected=NumberFormatException.class)
    public void testInvalid_13_EmptyString() { TypeConversion.stringToInteger(""); }
}
