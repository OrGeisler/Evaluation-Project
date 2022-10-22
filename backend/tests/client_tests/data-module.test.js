const dataModule = require("../../../client/build/jsfiles/data-module")

test("isEven should return true if number is even, false otherwise",function () {
    const value = new dataModule()
    expect(value.isEven(2)).toBeTruthy()
    expect(value.isEven(3)).toBeFalsy();
    expect(value.isEven("string")).toBeFalsy();
})