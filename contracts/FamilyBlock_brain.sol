// SPDX-License-Identifier: MIT

pragma solidity ^0.6.0;

import "./FamilyBlock.sol";

contract FamilyBlock_brain is FamilyBlock {
    FamilyBlock[] public FamilyBlockArray;

    function createFamilyBlockContract() public {
        FamilyBlock familyblock = new FamilyBlock();
        FamilyBlockArray.push(familyblock);
    }

    function sfStore(
        uint256 _familyblockIndex,
        string memory _name,
        string memory _age,
        string memory _dob,
        string memory _birthPlace,
        int256 _id
    ) public {
        // Address
        // ABI
        //this line has an explicit cast to the address type and initializes a new FamilyBlock object from the address
        FamilyBlock(address(FamilyBlockArray[_familyblockIndex])).addPerson(
            _name,
            _age,
            _dob,
            _birthPlace,
            _id
        );

        //this line simply gets the FamilyBlock object at the index _simpleStorageIndex in the array FamilyBlockArray
        //FamilyBlockArray[_simpleStorageIndex].store(_simpleStorageNumber);
    }

    function sfGet(uint256 _familyblockIndex) public view returns (int256) {
        //this line has an explicit cast to the address type and initializes a new FamilyBlock object from the address
        return
            FamilyBlock(address(FamilyBlockArray[_familyblockIndex])).getTree();

        //this line simply gets the FamilyBlock object at the index _simpleStorageIndex in the array simpleStorageArray
        //return simpleStorageArray[_simpleStorageIndex].retrieve();
    }
}
