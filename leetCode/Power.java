package leetCode;

public class Power {
	double base;
	double power;

	public Power(double base, double power) {
		this.base = base;
		this.power = power;
	}

	public double findPow() {
		double result = 1;
		for (int i = 0; i < Math.abs(power); i++) {
			result *= Math.abs(this.base);
		}

		if (this.power < 0)
			return 1 / result;
		else
			return result;
	}

	public static void main(String[] args) {
		Power test = new Power(2, -2);
		System.out.println(test.findPow());
	}
}
