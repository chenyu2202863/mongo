/**
 *    Copyright (C) 2013 MongoDB Inc.
 *
 *    This program is free software: you can redistribute it and/or  modify
 *    it under the terms of the GNU Affero General Public License, version 3,
 *    as published by the Free Software Foundation.
 *
 *    This program is distributed in the hope that it will be useful,
 *    but WITHOUT ANY WARRANTY; without even the implied warranty of
 *    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 *    GNU Affero General Public License for more details.
 *
 *    You should have received a copy of the GNU Affero General Public License
 *    along with this program.  If not, see <http://www.gnu.org/licenses/>.
 *
 *    As a special exception, the copyright holders give permission to link the
 *    code of portions of this program with the OpenSSL library under certain
 *    conditions as described in each individual source file and distribute
 *    linked combinations including the program with the OpenSSL library. You
 *    must comply with the GNU Affero General Public License in all respects for
 *    all of the code used other than as permitted herein. If you modify file(s)
 *    with this exception, you may extend this exception to your version of the
 *    file(s), but you are not obligated to do so. If you do not wish to do so,
 *    delete this exception statement from your version. If you delete this
 *    exception statement from all source files in the program, then also delete
 *    it in the license file.
 */

/**
 * This file contains tests for mongo/db/query/list_parsed_query.h
 */

#include "mongo/db/query/lite_parsed_query.h"

#include <sstream>
#include "mongo/db/json.h"
#include "mongo/unittest/unittest.h"

using std::stringstream;
using namespace mongo;

namespace {

    TEST(LiteParsedQueryTest, InitSortOrder) {
        LiteParsedQuery* lpq = NULL;
        Status result = LiteParsedQuery::make("testns", 0, 1, 0, BSONObj(), BSONObj(),
                                              fromjson("{a: 1}"), BSONObj(), &lpq);
        ASSERT_OK(result);
    }

    TEST(LiteParsedQueryTest, InitSortOrderString) {
        LiteParsedQuery* lpq = NULL;
        Status result = LiteParsedQuery::make("testns", 0, 1, 0, BSONObj(), BSONObj(),
                                              fromjson("{a: \"\"}"), BSONObj(), &lpq);
        ASSERT_NOT_OK(result);
    }

    //
    // Text meta BSON element validation
    //

    bool isFirstElementTextMeta(const char* sortStr) {
        BSONObj sortObj = fromjson(sortStr);
        BSONElement elt = sortObj.firstElement();
        bool result = LiteParsedQuery::isTextMeta(elt);
        return result;
    }

    // Check validation of $meta expressions
    TEST(LiteParsedQueryTest, IsTextMeta) {
        // Valid text meta sort
        ASSERT(isFirstElementTextMeta("{a: {$meta: \"text\"}}"));

        // Invalid text meta sorts
        ASSERT_FALSE(isFirstElementTextMeta("{a: {$meta: 1}}"));
        ASSERT_FALSE(isFirstElementTextMeta("{a: {$meta: \"image\"}}"));
        ASSERT_FALSE(isFirstElementTextMeta("{a: {$world: \"text\"}}"));
        ASSERT_FALSE(isFirstElementTextMeta("{a: {$meta: \"text\", b: 1}}"));
    }

    void testSortOrder(bool expectedValid, const char* expectedStr, const char* sortStr) {
        BSONObj sortOrder = fromjson(sortStr);
        bool valid = LiteParsedQuery::isValidSortOrder(sortOrder);
        if (expectedValid != valid) {
            stringstream ss;
            ss << sortStr << ": unexpected validation result. Expected: " << expectedValid;
            FAIL(ss.str());
        }
        BSONObj normalizedSortOrder = LiteParsedQuery::normalizeSortOrder(sortOrder);
        if (fromjson(expectedStr) != normalizedSortOrder) {
            stringstream ss;
            ss << sortStr << ": unexpected normalization result. Expected: " << expectedStr
               << ". Actual: " << normalizedSortOrder.toString();
            FAIL(ss.str());
        }
    }

    //
    // Sort order validation and normalization
    // In a valid sort order, each element satisfies one of:
    // 1. a number with value 1
    // 2. a number with value -1
    // 3. isTextMeta
    //

    TEST(LiteParsedQueryTest, NormalizeAndValidateSortOrder) {
        // Valid sorts
        testSortOrder(true, "{}", "{}");
        testSortOrder(true, "{a: 1}", "{a: 1}");
        testSortOrder(true, "{a: -1}", "{a: -1}");
        testSortOrder(true, "{a: {$meta: \"text\"}}", "{a: {$meta: \"text\"}}");

        // Invalid sorts
        testSortOrder(false, "{a: 1}", "{a: 100}");
        testSortOrder(false, "{a: 1}", "{a: 0}");
        testSortOrder(false, "{a: -1}", "{a: -100}");
        testSortOrder(false, "{a: 1}", "{a: Infinity}");
        testSortOrder(false, "{a: -1}", "{a: -Infinity}");
        testSortOrder(false, "{a: 1}", "{a: true}");
        testSortOrder(false, "{a: 1}", "{a: false}");
        testSortOrder(false, "{a: 1}", "{a: null}");
        testSortOrder(false, "{a: 1}", "{a: {}}");
        testSortOrder(false, "{a: 1}", "{a: {b: 1}}");
        testSortOrder(false, "{a: 1}", "{a: []}");
        testSortOrder(false, "{a: 1}", "{a: [1, 2, 3]}");
        testSortOrder(false, "{a: 1}", "{a: \"\"}");
        testSortOrder(false, "{a: 1}", "{a: \"bb\"}");
        testSortOrder(false, "{a: 1}", "{a: {$meta: 1}}");
        testSortOrder(false, "{a: 1}", "{a: {$meta: \"image\"}}");
        testSortOrder(false, "{a: 1}", "{a: {$world: \"text\"}}");
        testSortOrder(false, "{a: 1}", "{a: {$meta: \"text\", b: 1}}");
    }

}  // namespace
