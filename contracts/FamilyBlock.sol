// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

contract FamilyBlock {
    struct People {
        string name;
        int256 age;
        string dob;
        string birthPlace;
        int256 id;
    }

    People[] public people;
    mapping(string => int256) public nameToid;

    function getPerson() public {}

    function addPerson(
        string memory _name,
        int256 _age,
        string memory _dob,
        string memory _birthPlace,
        int256 _id
    ) public {
        people.push(People(_name, _age, _dob, _birthPlace, _id));
        nameToid[_name] = _id;
    }

    function getTree() public {}
}
