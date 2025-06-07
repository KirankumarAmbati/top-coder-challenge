#!/usr/bin/env python3
"""
Black Box Legacy Reimbursement System Replica
Reverse-engineered from 1000 historical cases and employee interviews
"""

import sys

def calculate_reimbursement(days, miles, receipts):
    """
    Calculate reimbursement based on reverse-engineered legacy system logic.
    
    Key insights from analysis:
    1. Base rate decreases for longer trips but with bonuses for specific lengths
    2. Mileage at $0.58 per mile  
    3. Receipt processing with caps but special handling for very high amounts
    4. Trip length bonuses for 7-8 day and 12+ day trips
    
    Args:
        days (int): Trip duration in days
        miles (float): Total miles traveled
        receipts (float): Total receipt amount in dollars
    
    Returns:
        float: Calculated reimbursement amount
    """
    
    # Base day amount - decreases for longer trips
    if days <= 3:
        base = days * 100  # Full rate for short trips
    elif days <= 7:
        base = days * 90   # Slightly reduced rate for medium trips  
    elif days <= 10:
        base = days * 75   # Reduced rate for long trips
    else:
        base = days * 60   # Much reduced rate for very long trips
    
    # Mileage component - $0.58 per mile
    mileage = miles * 0.58
    
    # Receipt processing with tiered caps
    if receipts <= 100:
        # Lower receipts get 50% reimbursement
        receipt_comp = receipts * 0.5
    elif receipts <= 500:
        # Medium receipts get good rate
        receipt_comp = 50 + (receipts - 100) * 0.5
    elif receipts <= 1000:
        # Higher receipts get reduced rate
        receipt_comp = 250 + (receipts - 500) * 0.3
    elif receipts <= 2000:
        # Very high receipts get low rate
        receipt_comp = 400 + (receipts - 1000) * 0.1
    else:
        # Extremely high receipts get minimal rate (the "bug")
        receipt_comp = 500 + (receipts - 2000) * 0.02
    
    subtotal = base + mileage + receipt_comp
    
    # Trip length bonuses (from interview patterns)
    if days == 7 or days == 8:
        trip_bonus = 300  # Special bonus for week-long trips
    elif days >= 12:
        trip_bonus = 400  # Bonus for very long trips
    elif days == 5:
        trip_bonus = 100  # Small bonus for 5-day trips mentioned in interviews
    else:
        trip_bonus = 0
    
    total = subtotal + trip_bonus
    return round(total, 2)

def main():
    """Main function to handle command line arguments"""
    if len(sys.argv) != 4:
        print("Usage: python3 calculate_reimbursement.py <trip_duration_days> <miles_traveled> <total_receipts_amount>")
        sys.exit(1)
    
    try:
        days = int(sys.argv[1])
        miles = float(sys.argv[2])
        receipts = float(sys.argv[3])
        
        reimbursement = calculate_reimbursement(days, miles, receipts)
        print(reimbursement)
        
    except ValueError as e:
        print(f"Error: Invalid input - {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
