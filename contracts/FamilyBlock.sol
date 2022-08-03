// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;
pragma experimental ABIEncoderV2;

contract FamilyBlock {
    int256 age;

    struct People {
        string name;
        string age;
        string dob;
        string birthPlace;
        int256 id;
        string _parent1;
        string _parent2;
    }

    People[] public people;
    mapping(string => int256) public nameToid;

    function getPerson() public {}

    function addPerson(
        string memory _name,
        string memory _age,
        string memory _dob,
        string memory _birthPlace,
        int256 _id,
        string memory _parent1,
        string memory _parent2
    ) public {
        people.push(
            People(_name, _age, _dob, _birthPlace, _id, _parent1, _parent2)
        );
        nameToid[_name] = _id;
    }

    function getTree() external view returns (int256) {
        return age;
    }
}
