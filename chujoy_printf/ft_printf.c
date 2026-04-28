/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: vrafyan <marvin@42.fr>                     +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/04 15:21:53 by vrafyan           #+#    #+#             */
/*   Updated: 2026/03/04 15:21:55 by vrafyan          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "ft_printf.h"

void	struct_init(t_identifier *arr)
{
	arr[0].specifier = 'c';
	arr[0].func = handle_c;
	arr[1].specifier = 's';
	arr[1].func = handle_s;
	arr[2].specifier = 'd';
	arr[2].func = handle_int;
	arr[3].specifier = 'i';
	arr[3].func = handle_int;
	arr[4].specifier = 'u';
	arr[4].func = handle_u;
	arr[5].specifier = 'x';
	arr[5].func = handle_x;
	arr[6].specifier = 'X';
	arr[6].func = handle_x_up;
	arr[7].specifier = 'p';
	arr[7].func = handle_p;
	arr[8].specifier = '%';
	arr[8].func = handle_per;
	arr[9].specifier = 0;
	arr[9].func = NULL;
}

void	specifier_check(va_list *arg, const char flag, t_identifier *arr,
		int *ret_val)
{
	int	j;

	j = 0;
	while (arr[j].specifier)
	{
		if (flag == arr[j].specifier)
		{
			*ret_val += arr[j].func(arg);
			break ;
		}
		++j;
	}
}

int	exec(va_list *arg, const char *flag, t_identifier *arr)
{
	int	i;
	int	ret_val;

	i = 0;
	ret_val = 0;
	while (flag[i])
	{
		if (flag[i] == '%')
		{
			++i;
			if (!flag[i])
				break ;
			specifier_check(arg, flag[i], arr, &ret_val);
		}
		else
		{
			write(1, &flag[i], 1);
			++ret_val;
		}
		++i;
	}
	return (ret_val);
}

int	ft_printf(const char *flag, ...)
{
	t_identifier	arr[10];
	int				i;
	int				ret_val;
	va_list			arg;

	va_start(arg, flag);
	i = 0;
	struct_init(arr);
	ret_val = exec(&arg, flag, arr);
	va_end(arg);
	return (ret_val);
}
