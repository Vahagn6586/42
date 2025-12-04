/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi_base.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vchiling <vchiling@student.42yerevan.am>   +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/12/04 15:12:49 by vchiling          #+#    #+#             */
/*   Updated: 2025/12/04 17:23:42 by vchiling         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

int	ft_atoi_base(char *str, char *base);

int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (*(str + i))
		++i;
	return (i);
}

int	is_valid_base(char *base)
{
	int	i;
	int	j;

	i = 0;
	while (*(base + i))
	{
		if (*(base + i) == '+' || *(base + i) == '-'
				|| *(base + i) <= 32 || *(base + i) == 127)
			return (0);
		j = i + 1;
		while (*(base + j))
		{
			if (*(base + i) == *(base + j))
				return (0);
			++j;
		}
		++i;
	}
	return (i >= 2);
}

int	base_index(char c, char *base_src)
{
	int	i;

	i = 0;
	while (*(base_src + i))
	{
		if (*(base_src + i) == c)
			return (i);
		++i;
	}
	return (-1);
}

int	ft_atoi_base(char *str, char *base)
{
	int	sign;
	int	result;
	int	index;

	if (!is_valid_base(base))
		return (0);
	sign = 1;
	result = 0;
	while ((*str >= 9 && *str <= 13) || *str == ' ')
		str++;
	while (*str == '+' || *str == '-')
	{
		if (*str == '-')
			sign = -sign;
		str++;
	}
	while (*str)
	{
		index = base_index(*str, base);
		if (index == -1)
			break ;
		result = result * ft_strlen(base) + index;
		++str;
	}
	return (result * sign);
}
/*
#include <stdio.h>

int ft_atoi_base(char *str, char *base);

int main(void)
{
    char *str1 = "1010";
    char *str2 = "FF";
    char *str3 = "-1A";
    char *str4 = "42";
    char *str5 = "123";

    char *bin = "01";
    char *hex = "0123456789ABCDEF";
    char *dec = "0123456789";

    printf("Binary %s -> %d\n", str1, ft_atoi_base(str1, bin));
    printf("Hex %s -> %d\n", str2, ft_atoi_base(str2, hex));
    printf("Hex negative %s -> %d\n", str3, ft_atoi_base(str3, hex));
    printf("Decimal %s -> %d\n", str4, ft_atoi_base(str4, dec));
    printf("Decimal %s -> %d\n", str5, ft_atoi_base(str5, dec));

    // Invalid digit test
    printf("Invalid digit test: %s -> %d\n", "1G", ft_atoi_base("1G", hex));

    return 0;
}
*/
