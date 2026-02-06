#!/usr/bin/env python3
"""
🧙‍♂️ The Fibonacci Spell - Ancient Magic of Number Sequences
==========================================================

This mystical scroll contains the power to generate the sacred Fibonacci sequence,
where each number is the sum of the two preceding ones, starting from 0 and 1.

The sequence reveals the golden ratio hidden within nature itself!
"""

def fibonacci_spell(n):
    """
    Cast the Fibonacci spell to generate the first n numbers of the sequence.
    
    Args:
        n (int): Number of Fibonacci numbers to generate
    
    Returns:
        list: The first n Fibonacci numbers
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    
    # Initialize the mystical sequence
    fib_sequence = [0, 1]
    
    # Cast the spell to generate remaining numbers
    for i in range(2, n):
        next_number = fib_sequence[i-1] + fib_sequence[i-2]
        fib_sequence.append(next_number)
    
    return fib_sequence

def display_magical_fibonacci(n=10):
    """
    Display the Fibonacci sequence with mystical formatting.
    """
    print("✨" * 40)
    print("🧙‍♂️  THE FIBONACCI SPELL IS CAST!  🧙‍♂️")
    print("✨" * 40)
    print()
    
    sequence = fibonacci_spell(n)
    
    print(f"Behold! The first {n} numbers of the sacred Fibonacci sequence:")
    print()
    
    for i, num in enumerate(sequence):
        print(f"Position {i+1:2d}: {num:8d}")
    
    print()
    print("🌟 The sequence:", sequence)
    print()
    
    # Show the golden ratio approximation
    if len(sequence) >= 2:
        ratio = sequence[-1] / sequence[-2] if sequence[-2] != 0 else 0
        golden_ratio = (1 + 5**0.5) / 2
        print(f"📐 Ratio of last two numbers: {ratio:.6f}")
        print(f"🏆 The Golden Ratio (φ):      {golden_ratio:.6f}")
        print(f"🎯 Difference:                {abs(ratio - golden_ratio):.6f}")
    
    print("✨" * 40)

if __name__ == "__main__":
    # Cast the spell for 10 numbers
    display_magical_fibonacci(10)