# Considerations for producing a good SRS
The following document is a skimmed version of `IEEE830-1993`. The ideal document was skimmed to answer the questions relative to this project (i.e. Final Year Project).

- [Nature of the SRS](#nature-of-the-srs)
- [Environment of the SRS](#environment-of-the-srs)
- [Characteristics of a good SRS](#characteristics-of-a-good-srs)
- [Joint preparation of the SRS](#joint-preparation-of-the-srs)
- [SRS evolution](#srs-evolution)
- [Prototyping](#prototyping)
- [Embedding design in the SRS](#embedding-design-in-the-srs)
- [Embedding project requirements in the SRS](#embedding-project-requirements-in-the-srs)

## Nature of the SRS
The basic issues that the SRS writer(s) shall address are the following:

- _Functionality_. What is the software supposed to do?
- _External interfaces_. How does the software interact with people, the system's hardware, other hardware, and other software?
- _Performance_. What is the speed, availability, response time, recovery time of various software functions, etc.?
- _Attributes_. What are the portability, correctness, maintainability, security, etc. considerations?
- _Design constraints imposed on an implementation_. Are there any required standards in effect, implementation language, policies for database integrity, resource limits, operating environment(s) etc.?

The SRS writer(s) should avoid placing either design or project requirements in the SRS.

## Environment of the SRS
Since the SRS has a specific role to play in the software development process, SRS writer(s) should be careful not to go beyond the bounds of that role. This means the SRS
- Should correctly define all of the software requirements. A software requirement may exist because of the nature of the task to be solved or because of a special characteristic of the project.
- Should not describe any design or implementation details. These should be described in the design stage of the project.
- Should not impose additional constraints on the software. These are properly specified in other documents such as a software quality assurance plan.

Therefore, a properly written SRS limits the range of valid designs, but does not specify any particular design.

## Characteristics of a good SRS
An SRS should be
- Correct
- Unambiguous
- Complete
- Consistent
- Ranked for importance and/or stability
- Verifiable
- Modifiable
- Traceable

### Correct
An SRS is correct if, and only if, every requirement stated therein is one that the software shall meet.

There is no tool or procedure that assures correctness. The SRS should be compared with any applicable superior specification, such as a system requirements specification, with other project documentation, and with other applicable standards, to assure that it agrees. Alternatively the customer or user can determine if the SRS correctly reflects the actual needs. Traceability makes this procedure easier and less prone to error.

### Unambiguous

An SRS is unambiguous if, and only if, every requirement stated therein has only one interpretation. As a minimum, this requires that each characteristic of the final product be described using a single unique term. In cases where a term used in a particular context could have multiple meanings, the term should be included in a glossary where its meaning is made more specific.

The SRS should be unambiguous both to those who create it and to those who use it.

#### Natural Language Pitfalls
Requirements are often written in natural language (for example, English). Natural language is inherently ambiguous. A natural language SRS should be reviewed by an independent party to identify ambiguous use of language so that it can be corrected.

#### Requirements specification languages
One way to avoid the ambiguity inherent in natural language is to write the SRS in a particular requirements specification language. Its language processors automatically detect many lexical, syntactic, and semantic errors.

#### Representation tools
In general, requirements methods and languages and the tools that support them fall into three general categories

##### Object
Object-oriented approaches organize the requirements in terms of real-world objects, their attributes, and the services performed by those objects.

##### Process
Process-based approaches organize the requirements into hierarchies of functions that communicate via dataflows.

##### Behavioral
Behavioral approaches describe external behavior of the system in terms of some abstract notion (such as predicate calculus), mathematical functions, or state machines.

When using any of these approaches it is best to retain the natural language descriptions. That way, customers unfamiliar with the notations can still understand the SRS.

### Complete
An SRS is complete if, and only if, it includes the following elements:

- All significant requirements, whether relating to functionality, performance, design constraints, attributes, or external interfaces. In particular any external requirements placed by a system specification should be acknowledged and treated.
- Definition of the responses of the software to all realizable classes of input data in all realizable classes of situations. Note that it is important to specify the responses to both valid and invalid input values.
- Full labels and references to all figures, tables, and diagrams in the SRS and definition of all terms and units of measure.

#### Use of TBDs
Any SRS that uses the phrase to be determined (TBD) is not a complete SRS. The TBD is, however, occasionally necessary and should be accompanied by

- A description of the conditions causing the TBD (for example, why an answer is not known) so that the situation can be resolved
- A description of what must be done to eliminate the TBD, who is responsible for its elimination, and by when it must be eliminated

### Consistent
### Ranked for importance and/or stability
### Verifiable
### Modifiable
### Traceable

## Joint preparation of the SRS
## SRS evolution
## Prototyping
## Embedding design in the SRS
## Embedding project requirements in the SRS
