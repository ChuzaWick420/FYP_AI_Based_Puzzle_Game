# The parts of an SRS
- Table of contents
- Introduction
  - Purpose
  - Scope
  - Definitions, acronyms and abbreviations
  - Reference
  - Overview
- Overall description
  - Product perspective
  - Product functions
  - User characteristics
  - Constraints
  - Assumptions and dependencies
- Appendixes
- Index

# Table of contents
- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Scope](#scope)
  - [Definitions, acronyms and abbreviations](#definitions-acronyms-and-abbreviations)
  - [Reference](#reference)
  - [Overview](#overview)
- [Overall description](#overall-description)
  - [Product perspective](#product-perspective)
    - [System interfaces](#System-interfaces)
    - [User interfaces](#user-interfaces)
    - [Hardware interfaces](#hardware-interfaces)
    - [Software interfaces](#software-interfaces)
    - [Communications interfaces](#communications-interfaces)
    - [Memory constraints](#memory-constraints)
    - [Operations](#operations])
    - [Site adaptation requirements](#site-adaptation-requirements)
  - [Product functions](#product-functions)
  - [User characteristics](#user-characteristics)
  - [Constraints](#constraints)
  - [Assumptions and dependencies](#assumptions-and-dependencies)
  - [Apportioning of requirements](#apportioning-of-requirements)
- [Appendixes](#appendixes)
- [Index](#index)

# Introduction
The introduction of the SRS should provide an overview of the entire SRS.

## Purpose
This subsection should accomplish the following:

- Delineate the purpose of the particular SRS
- Specify the intended audience for the SRS

## Scope

This subsection should

- Identify the software product(s) to be produced by name (for example, Host DBMS, Report Generator etc.)
- Explain what the software product(s) will, and, if necessary, will not do
- Describe the application of the software being specified, including relevant benefits, objectives, and goals
- Be consistent with similar statements in higher-level specifications (for example, the system requirement specification), if they exist

## Definitions, acronyms and abbreviations
This subsection should provide the definitions of all terms, acronyms, and abbreviations required to interpret properly the SRS. This information may be provided by reference to one or more appendixes in the SRS or by reference to other documents.

## Reference

This subsection should

- Provide a complete list of all documents referenced elsewhere in the SRS
- Identify each document by title, report number (if applicable), date, and publishing organization
- Specify the sources from which the references can be obtained

## Overview
This subsection should

- Describe what the rest of the SRS contains
- Explain how the SRS is organized

# Overall description
This section of the SRS should describe the general factors that affect the product and its requirements. This section does not state specific requirements. Instead, it provides a background for those requirements, which are defined in detail in section 3, and makes them easier to understand.

This section usually consists of six subsections, as follows:

- Product perspective
- Product functions
- User characteristics
- Constraints
- Assumptions and dependencies
- Requirements subsets

## Product perspective

This subsection of the SRS should put the product into perspective with other related products. If the product is independent and totally self-contained, it should be so stated here. If the SRS defines a product that is a component of a larger system, as frequently occurs, then this subsection should relate the requirements of that larger system to functionality of the software and should identify interfaces between that system and the software.

A block diagram showing the major components of the larger system, interconnections, and external interfaces can be helpful.

This subsection should also describe how the software operates inside various constraints. For example,
these could include:

- System interfaces
- User interfaces
- Hardware interfaces
- Software interfaces
- Communications interfaces
- Memory constraints
- Operations
- Site adaptation requirements

### System interfaces

This should list each system interface and identify the functionality of the software to accomplish the system requirement and the interface description to match the system.

### User interfaces

- The logical characteristics of each interface between the software product and its users. This includes those configuration characteristics (e.g., required screen formats, page or window layouts, content of any reports or menus, or availability of programmable function keys) necessary to accomplish the software requirements.
- All the aspects of optimizing the interface with the person who must use the system. This may simply comprise a list of do's and don'ts on how the system will appear to the user. One example may be a requirement for the option of long or short error messages. Like all others, these requirements should be verifiable, for example, "a clerk typist grade 4 can do function X in Z min after 1 h of rather than "a typist can do function X." (This may also be specified in the Software System Attributes under a section titled Ease of Use.)

### Hardware interfaces

This should specify the logical characteristics of each interface between the software product and the hardware components of the system. This includes configuration characteristics (number of ports, instruction sets, etc.) It also covers such matters as what devices are to be supported, how they are to be supported, and protocols. For example, terminal support may specify full screen support as opposed to line by line.

### Software interfaces

This should specify the use of other required software products (for example, a data management system, an operating system, or a mathematical package), and interfaces with other application systems (for example, the linkage between an accounts receivable system and a general ledger system). For each required software product, the following should be provided:

- Name
- Mnemonic
- Specification number
- Version number
- Source

For each interface, the following should be provided:

- Discussion of the purpose of the interfacing software as related to this software product.
- Definition of the interface in terms of message content and format. It is not necessary to detail any well-documented interface, but a reference to the document defining the interface is required.

### Communications interfaces

This should specify the various interfaces to communications such as local network protocols, etc.

### Memory constraints

This should specify any applicable characteristics and limits on primary and secondary memory.

### Operations

This should specify the normal and special operations required by the user such as

- The various modes of operations in the user organization; for example user-initiated operations
- Periods of interactive operations and periods of unattended operations
- Data processing support functions
- Backup and recovery operations

> [!NOTE]
> This is sometimes specified as part of the User Interfaces section.

### Site adaptation requirements

This could

- Define the requirements for any data or initialization sequences that are specific to a given site, mission, or operational mode, for example, grid values, safety limits, etc.
- Specify the site or mission-related features that should be modified to adapt the software to a particular installation.

## Product functions

This subsection of the SRS should provide a summary of the major functions that the software will perform. For example, an SRS for an accounting program may use this part to address customer account maintenance, customer statement, and invoice preparation without mentioning the vast amount of detail that each of those functions requires.

Sometimes the function summary that is necessary for this part can be taken directly from the section of the higher level specification (if one exists) that allocates particular functions to the software product. Note that for the sake of clarity:

- The functions should be organized in a way that makes the list of functions understandable to the customer or to anyone else reading the document for the first time.
- Textual or graphical methods can be used to show the different functions and their relationships. Such a diagram is not intended to show a design of a product but simply shows the logical relationships among variables.

## User characteristics

This subsection of the SRS should describe those general characteristics of the intended users of the product including educational level, experience, and technical expertise. It should not be used to state specific requirements but rather should provide the reasons why certain specific requirements are later specified in section 3 of the SRS.

## Constraints

This subsection of the SRS should provide a general description of any other items that will limit the developer's options. These include

- Regulatory policies
- Hardware limitations (for example, signal timing requirements)
- Interfaces to other applications
- Parallel operation
- Audit functions
- Control functions
- Higher-order language requirements
- Signal handshake protocols (for example, XON-XOFF, ACK-NACK)
- Reliability requirements
- Criticality of the application
- Safety and security considerations

## Assumptions and dependencies

This subsection of the SRS should list each of the factors that affect the requirements stated in the SRS. These factors are not design constraints on the software but are, rather, any changes to them that can affect the requirements in the SRS. For example, an assumption may be that a specific operating system will be available on the hardware designated for the software product. If, in fact, the operating system is not available, the SRS would then have to change accordingly.

## Apportioning of requirements
This subsection of the SRS should identify requirements that may be delayed until future versions of the system.

# Appendixes
# Index
