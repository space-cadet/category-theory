# Introduction to K-Linear Categories

## Table of Contents

---

1. [What are K-linear categories?](#what-are-k-linear-categories)
2. [TQFT and K-linear categories](#tqft-and-k-linear-categories)
3. [Structured Cobordisms](#structured-cobordisms)
4. [ADM Formalism and Category Theory](#adm-formalism-and-category-theory)
5. [Category of Group Representations](#category-of-group-representations)

## What are K-linear categories? <a name="what-are-k-linear-categories"></a>

$K$-linear categories are a mathematical structure that combines category theory with linear algebra over a field $K$.

A $K$-linear category is a category where:

- The morphism sets (the sets of maps between any two objects) are vector spaces over the field $K$
- Composition of morphisms is bilinear over $K$

In simpler terms, a $K$-linear category is like a category where:

- You can add morphisms together
- You can multiply morphisms by scalars from the field $K$
- These operations behave nicely with respect to composition

These structures are important in:

- Representation theory
- Mathematical physics (particularly in topological quantum field theory)
- Certain branches of algebra

They provide a framework for studying linear structures in a categorical setting, allowing techniques from both category theory and linear algebra to be combined.

## TQFT and K-linear categories <a name="tqft-and-k-linear-categories"></a>

K-linear categories play a fundamental role in Topological Quantum Field Theory (TQFT). Let me explain their significance:

In TQFT, we're interested in creating mathematical models that capture the essential features of quantum field theories while preserving topological invariance. K-linear categories provide the perfect mathematical framework for this purpose.

A TQFT can be understood as a functor from a category of cobordisms to a k-linear category (typically vector spaces over a field k). Here's why this is important:

Structural Framework: K-linear categories allow us to represent physical states as objects and physical processes as morphisms, while maintaining the vector space structure needed for quantum mechanics.
Invariants from Functors: The functor structure preserves composition, ensuring that gluing physical processes together (composing cobordisms) corresponds correctly to composing the associated linear maps.

## Structured Cobordisms <a name="structured-cobordisms"></a>

When manifolds have additional geometric structure, we define cobordisms that respect or extend this structure:

Riemannian cobordisms:
Objects are (n-1)-manifolds with Riemannian metrics
Morphisms are n-dimensional cobordisms with Riemannian metrics that restrict to the specified metrics on the boundaries
These are relevant for quantum field theories that depend on geometry, like certain sigma models
Cobordisms with connection:
Objects are manifolds equipped with connections (or principal G-bundles with connection)
Morphisms are cobordisms with connections that restrict appropriately to the boundary
These appear in gauge theories like Chern-Simons theory
Spin cobordisms:
Objects are manifolds with spin structures
Morphisms preserve or extend these spin structures
Crucial for fermionic quantum field theories

## ADM Formalism and Category Theory <a name="adm-formalism-and-category-theory"></a>

Developing a functorial formalism that maps General Relativity in the ADM (Arnowitt-Deser-Misner) formalism to a categorical picture is indeed a compelling research area with significant potential. Let me explore this possibility:

Connecting ADM Formalism to Categorical Structures
The ADM formalism already has a structure that seems amenable to categorification:

Objects as Spatial Slices: In ADM, spacetime is foliated into spatial 3-manifolds (Σt) evolving through time. These could naturally become objects in a category.
Morphisms as Spacetime Regions: The 4-dimensional regions between spatial slices could serve as morphisms between these objects.
Canonical Variables: The ADM variables (spatial metric hij and conjugate momentum πij) provide a phase space structure on each slice.

## Category of Group Representations <a name="category-of-group-representations"></a>

The category of representations of a group G, denoted Rep(G), is a fundamental example of a k-linear category:

Objects: Representations of G, which are vector spaces V equipped with a group homomorphism ρ: G → GL(V)
Morphisms: G-equivariant linear maps (maps that commute with the group action)
k-linear structure: The space of morphisms between two representations forms a vector space, and composition is bilinear

This category has rich additional structure:

It's monoidal (has tensor products of representations)
It has duals (conjugate representations)
For finite groups, it's semisimple (representations decompose into irreducibles)

Connection to TQFTs
In the context of TQFTs:

Chern-Simons Theory: For a compact Lie group G at level k, the associated TQFT uses a category of representations of the quantum group Uq(g), where g is the Lie algebra of G and q is a root of unity related to k. This is the mathematical foundation for many 3D topological invariants.
Reshetikhin-Turaev Construction: Starts with a modular tensor category (like Rep(Uq(g)) at appropriate q) and produces 3-manifold invariants and TQFTs.
Tangle Invariants: Using Rep(G) or its quantum version, we can construct invariants of tangles and links via diagrammatic calculus.
